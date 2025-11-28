# Thesis Manuscript Roadmap

## Overview

- **Target**: 10-15 pages introduction (English), then French translation
- **Advisor**: Emmanuel Gobet (+ Alain Durmus for Ch.5)
- **Timeline**: ~15 days per Emmanuel's estimate

---

## Manuscript Structure

| Chapter | Title | Status |
|---------|-------|--------|
| 1 | Introduction (English) | **TODO** — outline ready |
| 2 | Introduction (French) | TODO — translate Ch.1 when done |
| 3 | Heavy-Tailed GANs (HTGAN) | TODO — import from `~/proj/htgan` |
| 4 | Generative Neural Order Statistics (GENOS) | TODO — import from `~/proj/genos` |
| 5 | Gradient-Free Diffusion Fine-Tuning | TODO — import from `~/proj/ftdiffusion` |

---

## Chapter 1: Introduction (English) — Detailed Tasks

### Section 1: Context and Motivation (~2 pages)
- [ ] Para 1: Etymology of "Statistik" — structure in data collection
- [ ] Para 2: Modern generative modeling (GANs, diffusions)
- [ ] Para 3: The problem — when structure matters (tails, ordering, rewards)
- [ ] Para 4: This thesis — theory-guided generative methods

### Section 2: Three Structural Regimes (~3-4 pages)
- [ ] §2.1 Extreme Values and Tail Dependence (~1 page)
  - [ ] The problem: tail dependence in finance
  - [ ] Why standard GANs fail (Lipschitz argument)
- [ ] §2.2 Order Statistics and Ranking Constraints (~1 page)
  - [ ] The problem: ranked portfolios, impact investing
  - [ ] Why standard methods fail (normalization breaks ordering)
- [ ] §2.3 Reward-Tilted Distributions (~1 page)
  - [ ] The problem: fine-tuning with rewards
  - [ ] Why backprop through reward is expensive

### Section 3: Generative Modeling Background (~2-3 pages)
- [ ] §3.1 GANs: minimax game, WGAN variants
- [ ] §3.2 Diffusion models: score matching, SDEs
- [ ] §3.3 Universal approximation and its limits

### Section 4: Contributions (~3-4 pages)
- [ ] §4.1 HTGAN: key insight + main theorem (informal)
- [ ] §4.2 GENOS: key insight + main theorem (informal)
- [ ] §4.3 FTDiffusion: key insight + main result (informal)

### Section 5: Organization (~1 page)
- [ ] Chapter summaries (Ch.3, Ch.4, Ch.5)
- [ ] Mention paper venues/status

---

## Chapter 2: Introduction (French)

- [ ] Translate Chapter 1 section by section
- [ ] No content changes (per Emmanuel's instructions)

---

## Chapters 3-5: Import Papers

### Chapter 3: HTGAN
- [ ] Import from `~/proj/htgan/htgan_latex/`
- [ ] Adapt formatting to thesis style
- [ ] Check cross-references to intro

### Chapter 4: GENOS
- [ ] Import from `~/proj/genos/tex/`
- [ ] Adapt formatting to thesis style
- [ ] Check cross-references to intro

### Chapter 5: FTDiffusion
- [ ] Import from `~/proj/ftdiffusion/tex/`
- [ ] Coordinate with Alain on final version
- [ ] Adapt formatting to thesis style

---

## Final Steps

- [ ] EDMH title page (page 1 must follow EDMH template)
- [ ] Abstract (English + French)
- [ ] Acknowledgments
- [ ] Bibliography: merge bib files from all projects
- [ ] Review by Emmanuel
- [ ] Address reviewer comments (especially Ch.3 structural issues)
- [ ] Final proofread

---

## Key Files

```
manuscript/
├── main.tex                      # Main document
├── chapters/
│   ├── 01_introduction.tex       # English intro (OUTLINE READY)
│   ├── 02_introduction_fr.tex    # French intro (placeholder)
│   ├── 03_htgan.tex              # HTGAN (placeholder)
│   ├── 04_genos.tex              # GENOS (placeholder)
│   └── 05_ftdiffusion.tex        # FTDiffusion (placeholder)
├── macros/
│   ├── def.tex
│   └── commands.tex
└── out/main.pdf                  # Compiled output
```

---

## References to Cite (Introduction)

- Goodfellow et al. 2014 (GANs)
- Ho et al. 2020 (DDPM)
- Song & Ermon (score matching)
- Embrechts, Klüppelberg, Mikosch (Modelling Extremal Events)
- Achenwall 1748 (etymology of Statistik)
- RLHF / DPO literature

---

## Notes

- Emmanuel does not want to re-read Ch.3-4 (already done)
- Ch.5 is "en cours" with Alain
- Reviewer comments on Ch.3 (GENOS workshop) need addressing
