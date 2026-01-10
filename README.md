# python-more-things

Advanced Python essentials for building GenAI systems — a practical, code-first repository covering the patterns and libraries you’ll use daily: Pydantic models and settings, advanced OOP, typing primitives like `Literal`, concurrency with threading and asyncio, and performance-minded optimizations.

## Goals
- Consolidate advanced Python topics needed to build GenAI apps and services
- Provide small, focused examples you can run locally
- Encourage best practices for correctness, scalability, and maintainability

## Topics Covered
- Pydantic: robust data validation, model composition, settings management
- Advanced OOP: `@classmethod`, `@staticmethod`, composition vs inheritance, clean APIs
- Typing: `Literal`, `TypedDict`, `Protocol`, generics, runtime type safety patterns
- Concurrency: `threading`, multi-threading with `concurrent.futures`, async I/O via `asyncio`
- Optimizations: profiling, caching, and pragmatic performance tips

## Repository Structure
- [main.py](main.py): quick runner and scratchpad
- [python_literals.py](python_literals.py): typing and `Literal` examples
- [oops/main.py](oops/main.py): advanced OOP patterns (`@classmethod`, `@staticmethod`, etc.)
- [pydantic_things/main.py](pydantic_things/main.py): Pydantic models and settings
- [python_typing/main.py](python_typing/main.py): broader typing features and patterns
- [optimizations/main.py](optimizations/main.py): performance and optimization snippets

## Requirements
- Python: 3.13+
- Dependencies (declared in [pyproject.toml](pyproject.toml)):
	- fastapi
	- pydantic
	- pydantic-settings
	- python-dotenv

Install with a fresh virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install fastapi pydantic pydantic-settings python-dotenv
```

## Quick Start
Run any module directly:

```bash
# OOP patterns
python oops/main.py

# Pydantic models and settings
python pydantic_things/main.py

# Typing (including Literal)
python python_typing/main.py
python python_literals.py

# Optimizations
python optimizations/main.py
```

Async I/O and threading examples are included across modules; look for `async def`, `asyncio.run()`, `Thread`, and `concurrent.futures` usage.

## How This Helps GenAI Work
- Data contracts: Use Pydantic to validate LLM inputs/outputs and config
- Concurrency: Stream responses, parallelize I/O-bound calls, and manage timeouts
- OOP design: Encapsulate providers, evaluators, and pipelines with clean interfaces
- Typing: Document prompt/response shapes and catch mistakes early

## Contributing
- Keep examples minimal and runnable.
- Prefer small, focused modules over monoliths.
- Add a short docstring and a one-paragraph README section for new topics.

## Roadmap
- More asyncio streaming and backpressure patterns
- Structured output parsing patterns for multiple LLM providers
- Caching and rate-limiting helpers for production workloads

