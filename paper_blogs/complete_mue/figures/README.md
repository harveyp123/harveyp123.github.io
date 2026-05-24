# Blog-post figures — source index

Each PNG in this folder is exported from a PDF in the paper's `figure/` tree.
This file maps every blog figure back to its source.

## Quick regenerate

```bash
cd blog_post/figures
python3 regenerate.py
```

Requires PyMuPDF (`pip install pymupdf`). The script reads from the paper's
`figure/` folder (resolved as `../../figure/` relative to itself), renders
the first page of each source PDF at the listed DPI with
`fitz.Page.get_pixmap`, and writes the PNG into the current folder.

If you add, remove, or rename a blog figure, edit the `FIGS` list in
[`regenerate.py`](regenerate.py) and also update the mapping table below.

## Mapping

Paths are relative to the repo root (`mue_git/`).

| Blog PNG | Source PDF | DPI | Used in `index.html` |
|---|---|---|---|
| `dense_sweep_lm_lr.png` | `figure/blog_post/gen7_text_dim_128_layer_32_dense_ffn_1_8_moe_sigmoid_activated_experts_lr_val_loss_step25k_line_only_dense_ffn_1_only.pdf` | 200 | "The dense calibration sweep" — LM, learning-rate scan |
| `dense_sweep_lm_wd.png` | `figure/blog_post/gen7_text_dim_128_layer_32_dense_ffn_1_8_moe_sigmoid_activated_experts_w_decay_val_loss_step25k_line_only_dense_ffn_1_only.pdf` | 200 | "The dense calibration sweep" — LM, weight-decay scan |
| `dense_sweep_lm_init.png` | `figure/blog_post/gen7_text_dim_128_layer_32_dense_ffn_1_8_moe_sigmoid_activated_experts_init_std_val_loss_step25k_line_only_dense_ffn_1_only.pdf` | 200 | "The dense calibration sweep" — LM, init-std scan |
| `dense_sweep_df_lr.png` | `figure/blog_post/dim_128_bs256_it100k_moe_sigmoid_activated_experts_scaling_final_dense_ffn_1_only.pdf` | 200 | "The dense calibration sweep" — DF, learning-rate scan |
| `dense_sweep_df_wd.png` | `figure/blog_post/dim_128_bs256_25k_dense_moe_weight_decay_scan_final_avg_loss_dense_ffn_1_only.pdf` | 200 | "The dense calibration sweep" — DF, weight-decay scan |
| `dense_sweep_df_init.png` | `figure/blog_post/dim_128_bs256_25k_dense_moe_init_std_scan_final_avg_loss_until_3e-1_dense_ffn_1_only.pdf` | 200 | "The dense calibration sweep" — DF, init-std scan |
| `activated_experts_lr_lm.png` | `figure/llms/gen7_text_dim_128_layer_32_dense_ffn_1_8_moe_sigmoid_activated_experts_lr_val_loss_step25k_line_only.pdf` | 200 | "Activated-experts: optima align" — LR sweep, LM |
| `activated_experts_lr_df.png` | `figure/diffusions/activated_shared_grouped_experts/dim_128_bs256_it100k_moe_sigmoid_activated_experts_scaling_final.pdf` | 200 | "Activated-experts: optima align" — LR sweep, DF |
| `activated_experts_wd_lm.png` | `figure/llms/gen7_text_dim_128_layer_32_dense_ffn_1_8_moe_sigmoid_activated_experts_w_decay_val_loss_step25k_line_only.pdf` | 200 | "Activated-experts: optima align" — weight-decay sweep, LM |
| `activated_experts_wd_df.png` | `figure/diffusions/df_std_wdecay/dim_128_bs256_25k_dense_moe_weight_decay_scan_final_avg_loss.pdf` | 200 | "Activated-experts: optima align" — weight-decay sweep, DF |
| `activated_experts_init_lm.png` | `figure/llms/gen7_text_dim_128_layer_32_dense_ffn_1_8_moe_sigmoid_activated_experts_init_std_val_loss_step25k_line_only.pdf` | 200 | "Activated-experts: optima align" — init-std sweep, LM |
| `activated_experts_init_df.png` | `figure/diffusions/df_std_wdecay/dim_128_bs256_25k_dense_moe_init_std_scan_final_avg_loss_until_3e-1.pdf` | 200 | "Activated-experts: optima align" — init-std sweep, DF |
| `activated_experts_initial_loss_lm.png` | `figure/llms/gen7_text_dim_128_layer_32_dense_ffn_1_8_moe_sigmoid_activated_experts_lr_initial_iterations_2_seed_avg_lr_1e-3_max_step_100.pdf` | 200 | "Activated-experts: optima align" — initial training-loss curves (first 100 steps), LM |
| `activated_experts_initial_loss_df.png` | `figure/diffusions/activated_shared_grouped_experts/dim_128_bs256_it100k_moe_sigmoid_activated_experts_scaling_initial_iterations_4_seed_avg_lr_1p6e-3_max_step_100.pdf` | 200 | "Activated-experts: optima align" — initial training-loss curves (first 100 steps), DF |
| `lr_sweep_capacity_lm.png` | `figure/llms/gen7_text_dim_128_layer_32_dense_ffn_1_4_moe_sigmoid_capacity_lr_val_loss_step25k_line_only.pdf` | 200 | "MoE architectural axes" — capacity scaling, LM |
| `lr_sweep_capacity_df.png` | `figure/diffusions/MoE_capacity/dim_128_bs256_it100k_moe_sigmoid_capacity_final.pdf` | 200 | "MoE architectural axes" — capacity scaling, DF |
| `lr_sweep_granularity_lm.png` | `figure/llms/gen7_text_dim_128_layer_32_dense_ffn_1_4_moe_sigmoid_granularity_lr_val_loss_step25k_line_only.pdf` | 200 | "MoE architectural axes" — granularity, LM |
| `lr_sweep_granularity_df.png` | `figure/diffusions/granularity/dim_128_bs256_it100k_moe_sigmoid_granularity_final_with_ffn4.pdf` | 200 | "MoE architectural axes" — granularity, DF |
| `lr_sweep_shared_lm.png` | `figure/llms/gen7_text_dim_128_layer_32_ffn_1_moe_sigmoid_shared_expert_lr_val_loss_step25k_line_only.pdf` | 200 | "MoE architectural axes" — shared-expert sweep, LM |
| `lr_sweep_shared_df.png` | `figure/diffusions/activated_shared_grouped_experts/dim_128_bs256_it100k_moe_shared_expert_scan_final.pdf` | 200 | "MoE architectural axes" — shared-expert sweep, DF |
| `lr_sweep_grouped_lm.png` | `figure/llms/gen7_text_dim_128_layer_32_ffn_1_moe_sigmoid_group_global_norm_lr_val_loss_step25k_line_only.pdf` | 200 | "MoE architectural axes" — group-balanced routing, LM |
| `lr_sweep_grouped_df.png` | `figure/diffusions/activated_shared_grouped_experts/dim_128_bs256_it100k_moe_gn_grouped_experts_scaling_final.pdf` | 200 | "MoE architectural axes" — group-balanced routing, DF |
| `lr_sweep_depth_lm.png` | `figure/llms/gen7_text_dim_128_layer_4_8_16_32_ffn_1_moe_16e4a_model_layer_lr_val_loss_step25k_line_only.pdf` | 200 | "MoE architectural axes" — depth, LM |
| `lr_sweep_depth_df.png` | `figure/diffusions/depth_width/dim_128_bs256_it100k_layer_lr_scaling_final_ft.pdf` | 200 | "MoE architectural axes" — depth, DF |
| `lr_sweep_width_lm.png` | `figure/llms/gen7_text_dim_128_256_512_1024_layer_32_ffn_1_moe_16e4a_model_width_lr_val_loss_step25k_line_only.pdf` | 200 | "MoE architectural axes" — backbone width, LM |
| `lr_sweep_width_df.png` | `figure/diffusions/depth_width/dim_128_bs256_it100k_moe_width_scaling_final_ft.pdf` | 200 | "MoE architectural axes" — backbone width, DF |
| `fixed_lr_llm_activated.png` | `figure/paper_loss_scaling/fixed_lr_llm_activated_experts_scaling.pdf` | 200 | "Fixed-LR scaling across MoE axes" — LM, activated experts |
| `fixed_lr_df_activated.png` | `figure/paper_loss_scaling/fixed_lr_diffusion_activated_experts_scaling.pdf` | 200 | "Fixed-LR scaling across MoE axes" — DF, activated experts |
| `fixed_lr_llm_capacity.png` | `figure/paper_loss_scaling/fixed_lr_llm_capacity_scaling.pdf` | 200 | "Fixed-LR scaling across MoE axes" — LM, capacity |
| `fixed_lr_df_capacity.png` | `figure/paper_loss_scaling/fixed_lr_diffusion_capacity_scaling.pdf` | 200 | "Fixed-LR scaling across MoE axes" — DF, capacity |
| `fixed_lr_llm_granularity.png` | `figure/paper_loss_scaling/fixed_lr_llm_granularity_scaling.pdf` | 200 | "Fixed-LR scaling across MoE axes" — LM, granularity |
| `fixed_lr_df_granularity.png` | `figure/paper_loss_scaling/fixed_lr_diffusion_granularity_scaling.pdf` | 200 | "Fixed-LR scaling across MoE axes" — DF, granularity |
| `fixed_lr_llm_layers.png` | `figure/paper_loss_scaling/fixed_lr_llm_layer_scaling.pdf` | 200 | "Fixed-LR scaling across MoE axes" — LM, layers |
| `fixed_lr_df_layers.png` | `figure/paper_loss_scaling/fixed_lr_diffusion_layer_scaling.pdf` | 200 | "Fixed-LR scaling across MoE axes" — DF, layers |
| `large_loss_256p.png` | `figure/diffusions/large_run/gr6_conv_mini_512p_dense_vs_moe_multiresolution_1_256_256_train_loss.pdf` | 200 | "Large-scale evidence" — 256P image training loss, dense vs. MoE |
| `large_loss_512p.png` | `figure/diffusions/large_run/gr6_conv_mini_512p_dense_vs_moe_multiresolution_1_512_512_train_loss.pdf` | 200 | "Large-scale evidence" — 512P image training loss, dense vs. MoE |
| `large_loss_240p_keyframe.png` | `figure/diffusions/large_run/gr6_conv_mini_512p_dense_vs_moe_multiresolution_4_240_432_train_loss.pdf` | 200 | "Large-scale evidence" — 240P key-frame training loss, dense vs. MoE |
| `large_loss_240p_video.png` | `figure/diffusions/large_run/gr6_conv_mini_512p_dense_vs_moe_multiresolution_57_240_432_train_loss.pdf` | 200 | "Large-scale evidence" — 240P 5s video training loss, dense vs. MoE |
| `large_speedup_256p.png` | `figure/diffusions/large_run/gr6_conv_mini_512p_dense_vs_moe_multiresolution_1_256_256_convergence_speedup_vs_dense_step.pdf` | 200 | "Large-scale evidence" — 256P image convergence speedup |
| `large_speedup_240p_video.png` | `figure/diffusions/large_run/gr6_conv_mini_512p_dense_vs_moe_multiresolution_57_240_432_convergence_speedup_vs_dense_step.pdf` | 200 | "Large-scale evidence" — 240P 5s video convergence speedup |
| `large_llm_train_loss.png` | `figure/llms/large_run/gen7_text_100b_dense_vs_moe_smoothed_train_loss.pdf` | 200 | "Large-scale" LLM trio — smoothed training loss |
| `large_llm_val_loss.png` | `figure/llms/large_run/gen7_text_100b_dense_vs_moe_val_loss.pdf` | 200 | "Large-scale" LLM trio — validation loss on C4 |
| `large_llm_speedup.png` | `figure/llms/large_run/gen7_text_100b_dense_vs_moe_convergence_speedup_vs_dense_step.pdf` | 200 | "Large-scale" LLM trio — convergence speedup vs. dense |

## Regenerating one figure manually

If you only want to refresh a single PNG, the per-figure recipe is:

```python
import fitz   # PyMuPDF
SRC = "/path/to/figure/paper_loss_scaling/fixed_lr_llm_capacity_scaling.pdf"
DST = "fixed_lr_llm_capacity.png"
DPI = 200

doc = fitz.open(SRC)
pix = doc[0].get_pixmap(matrix=fitz.Matrix(DPI/72, DPI/72), alpha=False)
pix.save(DST)
doc.close()
```

For the full set, just use [`regenerate.py`](regenerate.py) — it does the
same thing for every entry in the mapping table.

## Notes on the teaser

The big top-of-page teaser in `index.html` is **not** in this folder — it's
the inline `<svg viewBox="0 0 1900 1080">…</svg>` block in the post body. It
was authored directly in HTML so it scales as vector and uses the same Inter
font family as the surrounding page. No raster version is needed.

(If you later want a social-card preview image for `og:image` / `twitter:image`,
export the inline SVG — or the original `figure/teaser_figure/teaser.pdf` —
to a ~1200×630 PNG, add it here, and reinstate the meta tags in
`index.html`.)
