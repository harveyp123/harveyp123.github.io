#!/usr/bin/env python3
"""Regenerate every blog PNG from its source PDF in the paper's figure/ tree.

The mapping below is the single source of truth for which PDF feeds which
PNG. Update both this list and the table in `README.md` when figures are
added, removed, or renamed.

Usage:
    cd blog_post/figures
    python3 regenerate.py

Requires PyMuPDF (`pip install pymupdf`).
"""

import os
import sys

try:
    import fitz  # PyMuPDF
except ImportError:
    sys.stderr.write(
        "ERROR: PyMuPDF is required.\n"
        "  Install with:  pip install pymupdf\n"
    )
    sys.exit(1)


# Folders, relative to this script
HERE = os.path.abspath(os.path.dirname(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
SRC_ROOT = os.path.join(REPO, "figure")
DST = HERE


# (src_relative_to_figure/, dst_filename, dpi)
FIGS = [
    # ---------- Small-dense calibration sweeps (LR / WD / init std x LM / DF) ----------
    # These are the upstream "tune-dense-once" sweeps that produce the
    # reference hyperparameters used throughout the rest of the blog.
    ("blog_post/gen7_text_dim_128_layer_32_dense_ffn_1_8_moe_sigmoid_activated_experts_lr_val_loss_step25k_line_only_dense_ffn_1_only.pdf",
     "dense_sweep_lm_lr.png",            200),
    ("blog_post/gen7_text_dim_128_layer_32_dense_ffn_1_8_moe_sigmoid_activated_experts_w_decay_val_loss_step25k_line_only_dense_ffn_1_only.pdf",
     "dense_sweep_lm_wd.png",            200),
    ("blog_post/gen7_text_dim_128_layer_32_dense_ffn_1_8_moe_sigmoid_activated_experts_init_std_val_loss_step25k_line_only_dense_ffn_1_only.pdf",
     "dense_sweep_lm_init.png",          200),
    ("blog_post/dim_128_bs256_it100k_moe_sigmoid_activated_experts_scaling_final_dense_ffn_1_only.pdf",
     "dense_sweep_df_lr.png",            200),
    ("blog_post/dim_128_bs256_25k_dense_moe_weight_decay_scan_final_avg_loss_dense_ffn_1_only.pdf",
     "dense_sweep_df_wd.png",            200),
    ("blog_post/dim_128_bs256_25k_dense_moe_init_std_scan_final_avg_loss_until_3e-1_dense_ffn_1_only.pdf",
     "dense_sweep_df_init.png",          200),

    # ---------- Activated-experts sweeps (small-scale Bridge II evidence) ----------
    # Four panels matching the paper's fig:activated-experts-scaling layout:
    #   (a) LR sweep, (b) WD sweep, (c) init std sweep, (d) initial training loss
    # each paired LM (left) / DF (right).
    ("llms/gen7_text_dim_128_layer_32_dense_ffn_1_8_moe_sigmoid_activated_experts_lr_val_loss_step25k_line_only.pdf",
     "activated_experts_lr_lm.png",            200),
    ("diffusions/activated_shared_grouped_experts/dim_128_bs256_it100k_moe_sigmoid_activated_experts_scaling_final.pdf",
     "activated_experts_lr_df.png",            200),
    ("llms/gen7_text_dim_128_layer_32_dense_ffn_1_8_moe_sigmoid_activated_experts_w_decay_val_loss_step25k_line_only.pdf",
     "activated_experts_wd_lm.png",            200),
    ("diffusions/df_std_wdecay/dim_128_bs256_25k_dense_moe_weight_decay_scan_final_avg_loss.pdf",
     "activated_experts_wd_df.png",            200),
    ("llms/gen7_text_dim_128_layer_32_dense_ffn_1_8_moe_sigmoid_activated_experts_init_std_val_loss_step25k_line_only.pdf",
     "activated_experts_init_lm.png",          200),
    ("diffusions/df_std_wdecay/dim_128_bs256_25k_dense_moe_init_std_scan_final_avg_loss_until_3e-1.pdf",
     "activated_experts_init_df.png",          200),
    ("llms/gen7_text_dim_128_layer_32_dense_ffn_1_8_moe_sigmoid_activated_experts_lr_initial_iterations_2_seed_avg_lr_1e-3_max_step_100.pdf",
     "activated_experts_initial_loss_lm.png",  200),
    ("diffusions/activated_shared_grouped_experts/dim_128_bs256_it100k_moe_sigmoid_activated_experts_scaling_initial_iterations_4_seed_avg_lr_1p6e-3_max_step_100.pdf",
     "activated_experts_initial_loss_df.png",  200),

    # ---------- MoE architectural-axis LR sweeps (capacity / granularity /
    #            shared / grouped / depth / width) — show that LR optima
    #            persist across MoE architectural variants ----------
    ("llms/gen7_text_dim_128_layer_32_dense_ffn_1_4_moe_sigmoid_capacity_lr_val_loss_step25k_line_only.pdf",
     "lr_sweep_capacity_lm.png",         200),
    ("diffusions/MoE_capacity/dim_128_bs256_it100k_moe_sigmoid_capacity_final.pdf",
     "lr_sweep_capacity_df.png",         200),
    ("llms/gen7_text_dim_128_layer_32_dense_ffn_1_4_moe_sigmoid_granularity_lr_val_loss_step25k_line_only.pdf",
     "lr_sweep_granularity_lm.png",      200),
    ("diffusions/granularity/dim_128_bs256_it100k_moe_sigmoid_granularity_final_with_ffn4.pdf",
     "lr_sweep_granularity_df.png",      200),
    ("llms/gen7_text_dim_128_layer_32_ffn_1_moe_sigmoid_shared_expert_lr_val_loss_step25k_line_only.pdf",
     "lr_sweep_shared_lm.png",           200),
    ("diffusions/activated_shared_grouped_experts/dim_128_bs256_it100k_moe_shared_expert_scan_final.pdf",
     "lr_sweep_shared_df.png",           200),
    ("llms/gen7_text_dim_128_layer_32_ffn_1_moe_sigmoid_group_global_norm_lr_val_loss_step25k_line_only.pdf",
     "lr_sweep_grouped_lm.png",          200),
    ("diffusions/activated_shared_grouped_experts/dim_128_bs256_it100k_moe_gn_grouped_experts_scaling_final.pdf",
     "lr_sweep_grouped_df.png",          200),
    ("llms/gen7_text_dim_128_layer_4_8_16_32_ffn_1_moe_16e4a_model_layer_lr_val_loss_step25k_line_only.pdf",
     "lr_sweep_depth_lm.png",            200),
    ("diffusions/depth_width/dim_128_bs256_it100k_layer_lr_scaling_final_ft.pdf",
     "lr_sweep_depth_df.png",            200),
    ("llms/gen7_text_dim_128_256_512_1024_layer_32_ffn_1_moe_16e4a_model_width_lr_val_loss_step25k_line_only.pdf",
     "lr_sweep_width_lm.png",            200),
    ("diffusions/depth_width/dim_128_bs256_it100k_moe_width_scaling_final_ft.pdf",
     "lr_sweep_width_df.png",            200),

    # ---------- Fixed-LR scaling grid (4 axes x 2 modalities) ----------
    ("paper_loss_scaling/fixed_lr_llm_activated_experts_scaling.pdf",
     "fixed_lr_llm_activated.png",       200),
    ("paper_loss_scaling/fixed_lr_diffusion_activated_experts_scaling.pdf",
     "fixed_lr_df_activated.png",        200),
    ("paper_loss_scaling/fixed_lr_llm_capacity_scaling.pdf",
     "fixed_lr_llm_capacity.png",        200),
    ("paper_loss_scaling/fixed_lr_diffusion_capacity_scaling.pdf",
     "fixed_lr_df_capacity.png",         200),
    ("paper_loss_scaling/fixed_lr_llm_granularity_scaling.pdf",
     "fixed_lr_llm_granularity.png",     200),
    ("paper_loss_scaling/fixed_lr_diffusion_granularity_scaling.pdf",
     "fixed_lr_df_granularity.png",      200),
    ("paper_loss_scaling/fixed_lr_llm_layer_scaling.pdf",
     "fixed_lr_llm_layers.png",          200),
    ("paper_loss_scaling/fixed_lr_diffusion_layer_scaling.pdf",
     "fixed_lr_df_layers.png",           200),

    # ---------- Large-scale multi-modal diffusion (4 losses + 2 speedups,
    #            matching the paper's fig:large-scale-complete-mue diffusion
    #            rows: 256P / 512P / 240P-keyframe / 240P-5s-video) ----------
    ("diffusions/large_run/gr6_conv_mini_512p_dense_vs_moe_multiresolution_1_256_256_train_loss.pdf",
     "large_loss_256p.png",                 200),
    ("diffusions/large_run/gr6_conv_mini_512p_dense_vs_moe_multiresolution_1_512_512_train_loss.pdf",
     "large_loss_512p.png",                 200),
    ("diffusions/large_run/gr6_conv_mini_512p_dense_vs_moe_multiresolution_4_240_432_train_loss.pdf",
     "large_loss_240p_keyframe.png",        200),
    ("diffusions/large_run/gr6_conv_mini_512p_dense_vs_moe_multiresolution_57_240_432_train_loss.pdf",
     "large_loss_240p_video.png",           200),
    ("diffusions/large_run/gr6_conv_mini_512p_dense_vs_moe_multiresolution_1_256_256_convergence_speedup_vs_dense_step.pdf",
     "large_speedup_256p.png",              200),
    ("diffusions/large_run/gr6_conv_mini_512p_dense_vs_moe_multiresolution_57_240_432_convergence_speedup_vs_dense_step.pdf",
     "large_speedup_240p_video.png",        200),

    # ---------- Large-scale LLM trio ----------
    ("llms/large_run/gen7_text_100b_dense_vs_moe_smoothed_train_loss.pdf",
     "large_llm_train_loss.png",         200),
    ("llms/large_run/gen7_text_100b_dense_vs_moe_val_loss.pdf",
     "large_llm_val_loss.png",           200),
    ("llms/large_run/gen7_text_100b_dense_vs_moe_convergence_speedup_vs_dense_step.pdf",
     "large_llm_speedup.png",            200),
]


def export(src_rel, dst_name, dpi):
    """Render the first page of `src_rel` to a PNG at the given DPI."""
    src = os.path.join(SRC_ROOT, src_rel)
    if not os.path.exists(src):
        print(f"  MISSING  {src_rel}", file=sys.stderr)
        return False
    doc = fitz.open(src)
    try:
        pix = doc[0].get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), alpha=False)
        pix.save(os.path.join(DST, dst_name))
        print(f"  OK       {dst_name:36s} ({pix.width}x{pix.height} @ {dpi} DPI)")
        return True
    finally:
        doc.close()


def main():
    print(f"Source root: {SRC_ROOT}")
    print(f"Destination: {DST}")
    print(f"Exporting {len(FIGS)} figures...\n")

    ok = sum(1 for src, dst, dpi in FIGS if export(src, dst, dpi))
    missing = len(FIGS) - ok

    print(f"\n{ok}/{len(FIGS)} regenerated, {missing} missing")
    return 0 if missing == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
