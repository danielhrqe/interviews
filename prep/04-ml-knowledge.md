# ML Knowledge - Prep Guide

> For: QuintoAndar (ML Interview + Coding) | Also useful for DoorDash ML system design
> Sources: [cola-entrevista.md](../companies/quintoandar/cola-entrevista.md), [cola-rapida.md](../companies/quintoandar/cola-rapida.md)

---

## 1. Concept Quick-Fire Flashcards (Self-Test)

Cover the answer column and test yourself. Goal: answer each in <15 seconds.

| # | Question | Answer |
|---|----------|--------|
| 1 | What is gradient descent? | Algorithm that minimizes model error iteratively. Learning rate = step size (hyperparameter) |
| 2 | High learning rate problem? | Error jumps around, never converges → decrease LR |
| 3 | Low learning rate problem? | Takes forever to converge → increase LR |
| 4 | Overfitting: what is it? | Model memorized training data. Train 99%, test 60% (big gap). Fix: regularization, reduce complexity |
| 5 | Underfitting: what is it? | Model didn't learn. Train 55%, test 50% (both bad). Fix: more complex model, more features |
| 6 | "More data" fixes overfitting? | **NO!** More data fixes drift. Overfitting → regularization (L1/L2) |
| 7 | Bias-Variance tradeoff? | High Bias = underfitting (too simple). High Variance = overfitting (too complex). Goal: balance both |
| 8 | K-Fold Cross-Validation? | Split into K parts, train on K-1, test on 1, repeat K times. Score = average. K=10 > K=5 |
| 9 | L1 vs L2 regularization? | L1 (Lasso): zeros out useless features (selection). L2 (Ridge): shrinks all weights. Both fight overfitting |
| 10 | Data Drift vs Concept Drift? | Data drift: INPUTS changed (new profiles). Concept drift: RELATIONSHIP changed (behavior shifted). Both → retrain |
| 11 | Classification vs Regression? | Classification: category (yes/no). Regression: continuous number (price). Gotcha: Logistic Regression = CLASSIFICATION |
| 12 | **Precision?** ⚠️ | Of those you ACCUSED, how many were CORRECT? (confidence in accusation) |
| 13 | **Recall?** ⚠️ | Of those that EXISTED, how many did you CATCH? (capture ability) |
| 14 | When prioritize Recall? | Fraud/security: don't let any escape |
| 15 | When prioritize Precision? | Financial planning: trust the prediction |
| 16 | F1 Score? | Harmonic mean of Precision and Recall |
| 17 | AUC-ROC? | Ability to separate classes. 0.5 = random guess, 1.0 = perfect |
| 18 | MAE vs RMSE? | MAE: avg error in reais. RMSE: penalizes large errors more |
| 19 | R²? | How much the model explains (0 to 1, closer to 1 = better) |
| 20 | NDCG? | Ranking quality: best items on top = high NDCG |
| 21 | MRR? | Position of first good result. Pos 1 = MRR 1.0, Pos 5 = MRR 0.2 |
| 22 | Supervised vs Unsupervised? | Supervised: has labels. Unsupervised: no labels, discovers patterns (K-Means) |
| 23 | Reinforcement Learning? | Learns by reward. Ex: optimize price in real time |
| 24 | CNN, RNN, Transformer? | CNN: images. RNN/LSTM: sequences. Transformer: attention mechanism, base of LLMs |
| 25 | What are Embeddings? | Text → numeric vector. Similar texts are close in vector space |
| 26 | What is RAG? | LLM + search in real company docs → reduces hallucination |
| 27 | Hyperparameter vs Parameter? | Hyper: engineer sets before training (LR, max_depth). Param: model learns (weights) |

⚠️ **Precision/Recall was weak spot (Feb 9)** — practice these until instant.

---

## 2. ML System Design Framework

### 7-Step Process

| Step | Time | What |
|------|------|------|
| 1. Problem Framing | 5 min | Business problem → ML problem. Classification? Regression? Ranking? |
| 2. Data | 5 min | What data exists? Volume? Quality? Labeling strategy? |
| 3. Features | 5 min | Feature engineering. Online vs offline features. Feature store? |
| 4. Model | 5 min | Model selection. Baseline → simple model → complex. Why this model? |
| 5. Training | 5 min | Pipeline: data → features → train → evaluate → register. MLflow/similar |
| 6. Serving | 5 min | Batch vs online inference. Latency requirements. A/B testing. Canary deploy |
| 7. Monitoring | 5 min | Metrics: model perf (precision/recall/NDCG) + data quality + infra (latency). Drift detection → retrain trigger |

### Quick Answers for Common ML System Design Questions

**"Model degraded, what do you do?"**
→ Investigate: data quality → data drift → concept drift → retrain with recent data → validate → canary deploy

**"How to monitor a model in production?"**
→ Model metrics (precision/recall), input distribution (detect drift), infra metrics (latency), alerts with threshold to trigger retraining

**"How to take a notebook to production?"**
→ Standardized templates (base classes) → PR review → CI/CD automated → deploy → monitoring. Trunk-based, 3-min to production

**"Data drift vs concept drift?"**
→ Data drift = inputs changed. Concept drift = relationship changed. Both need retraining with recent data

---

## 3. Platform Comparison (Your Stack vs QA Stack)

| Component | Your Platform | QuintoAndar |
|-----------|---------------|-------------|
| Compute | Databricks/Spark on K8s | Databricks (Spark) |
| Orchestration | Airflow (4K+ DAGs) | Airflow |
| Model Serving | K8s + ArgoCD | K8s-based |
| Experiment Tracking | MLflow | MLflow |
| Feature Store | Custom | Feature Store (internal) |
| Monitoring | Datadog | Kafka-based monitoring |
| IaC | Terraform/Terragrunt | Infrastructure as Code |
| CI/CD | GitHub Actions + ArgoCD | CI/CD pipeline |
| Development | Trunk-based, 3-min deploy | Trunk-based |

**The overlap is remarkable** — use this in your interview to show natural fit.

---

## 4. Precision/Recall Drill ⚠️

This was flagged as a weak spot (fixed after 5 attempts on Feb 9). Keep sharp.

### The Confusion Matrix
```
                  Predicted Positive    Predicted Negative
Actual Positive      TP (True Pos)       FN (False Neg)
Actual Negative      FP (False Pos)       TN (True Neg)
```

### Formulas
- **Precision** = TP / (TP + FP) → "Of my positive predictions, how many were right?"
- **Recall** = TP / (TP + FN) → "Of all actual positives, how many did I find?"

### Mnemonics
- **Precision** = **P**rediction quality → "Am I **p**recise when I say yes?"
- **Recall** = **R**etrieval completeness → "Did I **r**etrieve all the real ones?"

### Practice Scenarios
1. **Fraud detection**: Recall matters more (don't miss fraud). Accept some false alarms.
2. **Email spam filter**: Precision matters more (don't send real email to spam).
3. **Medical screening**: Recall matters more (don't miss a disease). Follow up confirms.
4. **Recommendation system**: Precision matters more (show relevant items).
5. **QuintoAndar ranking**: NDCG (good results on top), but precision/recall for individual models.

---

## 5. RAG System Design Template

This went well in the QA Tech Screening. Keep ready for future rounds.

### Architecture
```
User Query
    ↓
[Tokenization + Embedding] → Query Vector
    ↓
[Vector Database Search] → Top K relevant document chunks
    ↓
[Context Assembly] → Query + Retrieved Chunks
    ↓
[LLM Inference] → Generated Response
    ↓
[Post-processing] → Final Answer to User
```

### Key Components
| Component | Purpose | Options |
|-----------|---------|---------|
| Embedding Model | Convert text to vectors | OpenAI Ada, Sentence-BERT, custom |
| Vector DB | Similarity search | Pinecone, Weaviate, pgvector, FAISS |
| Chunk Strategy | Split docs into pieces | Fixed size, semantic, overlap |
| Retrieval | Find relevant chunks | Dense retrieval, hybrid (dense+sparse) |
| LLM | Generate answer | GPT-4, Claude, Llama, custom fine-tuned |
| Evaluation | Measure quality | Relevance, faithfulness, answer correctness |

### Trade-offs to Discuss
- Chunk size: small (precise) vs large (more context)
- Top K: fewer (precise) vs more (comprehensive, but noise)
- Embedding model: general (quick start) vs domain-specific (better quality)
- Vector DB: managed (Pinecone, easy) vs self-hosted (FAISS, cheap at scale)
- Hybrid search: dense + keyword (BM25) often beats pure dense retrieval

### Monitoring
- Retrieval quality: are chunks relevant to the query?
- Answer faithfulness: is the LLM answer grounded in retrieved docs?
- Latency: embedding time + search time + LLM time
- User feedback: thumbs up/down, clickthrough
