# Core Types of Prompting Techniques

According to *The Prompt Report* and major enterprise taxonomies, prompting methods generally cluster into six operational strategies:

| Prompt Type Category | Operational Strategy | Core Techniques Included |
| :--- | :--- | :--- |
| **In-Context Learning (ICL)** | Providing zero, one, or multiple demonstrations directly within the context window to alter behavior without updating weights. | • **Zero-Shot:** Direct querying without structural examples.<br>• **Few-Shot:** Presenting 3–5 input-output exemplars. |
| **Thought Generation** | Explicitly prompting the LLM to generate intermediate reasoning paths before issuing a final conclusion. | • **Chain-of-Thought (CoT):** Adding "think step-by-step" to resolve logic gaps.<br>• **Step-Back Prompting:** Prompting the LLM to identify a high-level abstract concept before tackling the specific problem. |
| **Decomposition** | Breaking complex, multi-variable logic problems down into branching trees or parallel execution routes. | • **Tree-of-Thoughts (ToT):** Allowing the model to evaluate and branch down multiple distinct reasoning pathways.<br>• **Least-to-Most:** Breaking a massive problem into sequential sub-problems. |
| **Ensembling** | Running multiple concurrent generations or thoughts and using an aggregation method to pick the best output. | • **Self-Consistency:** Sampling multiple alternate reasoning paths and using a majority vote for final selection. |
| **Self-Criticism & Loops** | Forcing the language model to analyze its own outputs against defined criteria or external feedback loops. | • **Self-Reflection / Reflexion:** Asking the AI to evaluate its draft for logical errors and rewrite its final answer accordingly. |
| **External/Agentic Tooling** | Forcing the LLM to orchestrate external software systems or retrieval systems. | • **ReAct Framework:** Alternating Reasoning loops with Action items (e.g., executing a web search or a Python script).<br>• **RAG (Retrieval-Augmented Generation):** Augmenting prompts dynamically with data pulled from vector databases. |
