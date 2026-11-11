# Core Types of Prompting Techniques

Core prompting techniques for Large Language Models (LLMs) fall into foundational, few-shot, reasoning, and structural categories:

## Foundational Prompting
* **Zero-Shot Prompting:** Giving a direct task or question with no background examples, relying entirely on the model's pre-trained knowledge (e.g., *"Translate this sentence to Spanish."*).
* **One-Shot & Few-Shot Prompting:** Providing a single example (*one-shot*) or 3 to 5 examples (*few-shot*) of input-output pairs inside the prompt to guide style, tone, and format.
* **Role / Persona Prompting:** Assigning a specific expert lens or identity to the AI (e.g., *"Act as a skeptical venture capitalist"*), which biases its tone, vocabulary, and analytical priorities.

## Reasoning & Logic Techniques
* **Chain-of-Thought (CoT) Prompting:** Forcing the model to articulate intermediate reasoning steps before giving a final answer by adding phrases like *"Let's think step by step"*.
* **Self-Consistency:** Generating multiple independent reasoning paths or answers for the same prompt and selecting the most consistent or frequent outcome.
* **Tree of Thoughts (ToT):** Allowing the model to explore multiple branches of thought or solution paths, evaluate their progress, and backtrack or look ahead for complex problem-solving.

## Workflow & Structure Techniques
* **Prompt Chaining:** Breaking a complex objective into a sequential pipeline of smaller, connected prompts where the output of one step feeds directly into the next.
* **Retrieval-Augmented Generation (RAG):** Grounding the model by injecting external documents, databases, or search results into the prompt context.
* **Instructional / Format Constraints:** Explicitly defining structural requirements within the prompt, such as demanding valid JSON, specific markdown tables, or strict word limits.

<br>

