# Complete-muE blog post

Standalone HTML draft of a blog post summarizing the paper
*Complete-muE: Optimal Hyperparameter Transfer and Scaling for MoE Models*
by Hongwu Peng, Ohiremen Dibua, Yuanjun Xiong, Yifan Gong, Jianming Zhang,
and Yan Kang (Adobe Research).

## Files

- `index.html` — the post itself. Self-contained except for MathJax (loaded
  from CDN).
- `style.css` — minimal, dependency-free stylesheet (no external fonts).
- `figures/` — 14 PNG figures exported from the paper's source PDFs (teaser,
  small-scale LR sweeps, 4×2 fixed-LR scaling grid, large-scale loss and
  convergence-speedup plots).
- `README.md` — this file.

## How to preview

Open `index.html` directly in a browser. Math rendering requires an internet
connection (MathJax is loaded from `cdn.jsdelivr.net`); everything else
(layout, images, fonts, favicon) works offline.

If you'd rather not depend on the CDN, swap the `<script>` tag in
`index.html` for a local copy of MathJax 3, or pre-render the math to SVG
with `mathjax-node` at build time.

## Reader tiers

The post is written to work for three audiences in one read-through:

1. **General reader** — hero, TL;DR, and "Why MoE tuning is so painful" build
   the problem from scratch. No prior MoE knowledge assumed.
2. **ML practitioner** — "The core insight," "The recipe in three steps,"
   and the results section are the actionable parts. The recipe is callout-
   styled so it's easy to find on a re-read.
3. **ML researcher** — "Under the hood" boxes carry the equations
   ($A(H) = d/H$, $\rho_B^{\mathrm{exp}} = \rho_D^{\mathrm{exp}}$, the
   $\sigma_0$ shift formula), and the calibration section flags the
   first-order-vs-second-order distinction explicitly.

The audience note right after the TL;DR points readers to the right
jumping-off point.

## Tone

The post deliberately mirrors the paper's calibrated framing:

- Claims the recipe works **and** flags the bounded $\sigma_0$ drift
  honestly.
- Connects the small-scale axis sweeps and the large-scale multimodal/LM
  runs as two complementary kinds of empirical evidence for the same "tune
  dense once, transfer to all" recipe.
- Uses concrete numbers from the paper ($4.5\times$ video speedup,
  $5.3\text{-}5.5\times$ LLM speedup) rather than hand-waving.

If you want a more marketing-flavored variant, the calibration section is
the first place to soften; if you want a more rigorous variant, expand the
"Under the hood" boxes with the SDE objects ($\sigma_0$,
$\widetilde\lambda$, $H_{\mathrm{SDE}}$) from Appendix A of the paper.

## Regenerating figures

Figures are PNGs exported from the paper's source PDFs at 180–200 DPI using
PyMuPDF. To regenerate:

```python
import fitz, os
src_root = "../figure"
dst = "figures"
# ... see git history or the script that originally produced these
```

The exported figures used are:

| File                              | Paper figure                                           |
|-----------------------------------|--------------------------------------------------------|
| `teaser.png`                      | Title-page teaser                                      |
| `activated_experts_lr_lm.png`     | LM activated-experts LR sweep (Bridge II evidence)     |
| `activated_experts_lr_df.png`     | Diffusion activated-experts LR sweep                   |
| `fixed_lr_{llm,df}_activated.png` | Fixed-LR scaling, activated experts (LM, DF)           |
| `fixed_lr_{llm,df}_capacity.png`  | Fixed-LR scaling, capacity (LM, DF)                    |
| `fixed_lr_{llm,df}_granularity.png` | Fixed-LR scaling, granularity (LM, DF)               |
| `fixed_lr_{llm,df}_layers.png`    | Fixed-LR scaling, layer depth (LM, DF)                 |
| `large_loss_240p_video.png`       | 240P 5s video diffusion training loss, dense vs. MoE   |
| `large_speedup_240p_video.png`    | 240P 5s video convergence speedup                      |
| `large_speedup_256p.png`          | 256P image convergence speedup (reserve / future use)  |

## Things to update before publishing

- **Public paper link.** "Read more" section currently says "Public link
  forthcoming." Replace with the actual arXiv / project-page URL when
  available.
- **Contact.** The footer / "Read more" section uses
  `hongwup@adobe.com` — change if a different point of contact is preferred.
- **Open Graph image.** Currently set to `figures/teaser.png`. If hosting on
  a real site, you may want a tighter aspect-ratio social-card image
  (1200×630).
- **CSP / sandboxing.** Some blog platforms forbid inline `<script>` tags.
  Either inline MathJax configuration in a separate file with appropriate
  CSP hashes, or pre-render math to SVG at build time.

## What's intentionally not in here

- A bibliography. The post references prior work in prose only; full
  citations are in the paper.
- The benchmark table from the paper (downstream LLM evals). Held back so
  the blog post focuses on the core claim — "tune dense once, transfer to
  all" — rather than ranking against baselines.
- Per-axis hyperparameter formulas (Tables 1 & 2 of the paper). The post
  points readers at the paper for the actual rules; spelling them out
  inline would lose the "one calibration → easy lookup" message.
