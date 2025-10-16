import os

import datasets
import verifiers as vf
from exa_py import Exa
from openai import AsyncOpenAI


def exa_search(query: str, num_results: int = 5) -> list[dict]:
    exa_client = Exa(api_key=os.getenv("EXA_API_KEY"))
    search_results: list[dict] = []
    for result in exa_client.search_and_contents(query, num_results=num_results, summary=True).results:
        search_results.append(
            {
                "title": result.title,
                "url": result.url,
                "summary": result.summary,
            }
        )
    return search_results

def load_environment(**kwargs) -> vf.Environment:
    dataset = datasets.load_dataset("willcb/wiki-trivia-questions", split="train") 
    # TODO: replace with real dataset with "question" and "answer" str columns
    judge_client = AsyncOpenAI(api_key=os.getenv("PRIME_API_KEY"), base_url="https://api.pinference.ai/api/v1")
    rubric = vf.JudgeRubric(
        judge_client = judge_client,
        judge_model = "openai/gpt-4.1-mini",
    )
    async def judge_reward(judge, prompt, completion, answer, state) -> float:
        judge_response = await judge(prompt, completion, answer, state)
        return 1.0 if "yes" in judge_response.lower() else 0.0
    rubric.add_reward_func(judge_reward, 1.0)
    vf_env = vf.ToolEnv(
        dataset=dataset,
        rubric=rubric,
        tools=[exa_search],
    )

    return vf_env