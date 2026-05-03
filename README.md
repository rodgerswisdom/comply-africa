# ComplyAfrica

&gt; Open-source compliance intelligence for African banks and fintechs.  
&gt; Built in Nairobi by the guy behind [Keverd](https://keverd.com).

**Status:** Early. Regulatory corpus in progress. APIs coming.  
**Ask:** Contribute a regulation, roast the approach, or tell us what we're missing.

---

## Why This Exists

I built [Keverd](https://keverd.com) to help African fintechs stop fraud. In every sales call, the same second problem came up: compliance is manual, expensive, and reactive.

- A Kenyan MFB spends 3 days preparing CBK returns every month
- A Nigerian fintech's compliance officer manually checks 4 websites for CBN circulars
- A Ghanaian startup got fined because they missed a BOG threshold change announced on Twitter

We need a shared, structured, machine-readable layer for African financial regulation.  
This is my attempt. Open source because compliance shouldn't be a monopoly.

---

## What's Here Now

| Component | Status | Description |
|-----------|--------|-------------|
| `/regulations/kenya/cbk` | 🟡 In Progress | Prudential guidelines, AML rules, returns |
| `/regulations/nigeria/cbn` | 🔴 Not started | Need contributors |
| `/patterns/mobile-money` | 🟡 In Progress | AML patterns for agent networks |
| `/reports/cbk-returns` | 🔴 Not started | Auto-generation templates |
| `/api` | 🔴 Not started | FastAPI layer (see Roadmap) |

---

## The Goal

**For compliance officers:**  
"Did any regulation change this week that affects my license?" → One query, one answer.

**For developers:**  
`POST /screen` → Check a customer against sanctions, PEPs, and adverse media in 200ms.  
`POST /generate` → Auto-draft a CBK return from your transaction CSV.  
`GET /changes` → See what changed in your regulator's rules this week.

**For regulators:**  
A standard format for publishing rules that machines can read. We will consume whatever you publish.

---

## Contributing

We need three things:

### 1. Regulatory Documents
Have a PDF, circular, or guideline from your central bank?  
Open an issue with `[REGULATION] Country: Regulator: Topic` and attach or link it.  
We will structure it and add it to the corpus.

### 2. Local Knowledge
Know which PEP list is actually used in Ghana?  
Know that CBK accepts returns in Excel but BOU wants PDF?  
Open an issue with `[CONTEXT] Country: What we need to know`.

### 3. Code
Python, FastAPI, data engineering. See `CONTRIBUTING.md` (coming).

---

## Roadmap

| Phase | Target | Deliverable |
|-------|--------|-------------|
| 0 | Now | Structured corpus for Kenya + Nigeria |
| 1 | June 2026 | `GET /regulations` API — query rules by country, license type, date |
| 2 | July 2026 | `POST /screen` MVP — sanctions + basic PEP |
| 3 | August 2026 | `POST /generate` MVP — CBK prudential returns |
| 4 | Q3 2026 | Community-validated, first paid API keys |

---

## Data Sovereignty & Ethics

- No customer data in this repo. Ever.  
- All regulatory text is public government publication.  
- We will support on-premise deployment for paranoid banks.  
- We will never sell screening data to third parties.

---

## Related

- [Keverd](https://keverd.com) — Device trust and fraud prevention for African fintechs
- [CMA Kenya Sandbox](https://sandbox.cma.or.ke) — Where we test

---

## Contact

- Issues: Right here
- Discussions: GitHub Discussions tab
- Twitter/X: [@hawona_4th](https://x.com/Hawona_4th) (DMs open)
- Email: trulhawona@gmail.com

---

**License:** MIT for code, CC BY for regulatory corpus.  
**Built by:** People who think African fintech infrastructure should be open, inspectable, and actually work.
