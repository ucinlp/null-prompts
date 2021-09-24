# Null Prompts

[![ucinlp](https://circleci.com/gh/ucinlp/null-prompts.svg?style=svg)](https://app.circleci.com/pipelines/github/ucinlp/null-prompts)

Codebase for "Cutting Down on Prompts and Parameters: Simple Few-Shot Learning
with Language Models" by Robert L. Logan IV, Ivana Balažević, Eric Wallace,
Fabio Petroni, Sameer Singh, and Sebastian Riedel.


## Getting Started

### Environment Setup

Install the `nullprompt` library into a fresh virtual environment.

```{bash}
conda create -n null-prompts python=3.8
conda install pytorch==1.4.0 -c pytorch -y
pip install -e .
```

### Few-Shot Data

The datasets used in our experiments can be downloaded from: TBD.


## Running Experiments

### Using `crossval.py`

YAML configs for the experiments in our paper are located in the `jobs/`
directory. To replicate one of these experiments run:

```{bash}
python -m nullprompt.crossval [PATH TO CONFIG]
```

### Using `trainers` Scripts

For more fine-grained control, e.g., if you would not like to run
cross-validation or only train or evaluate a model, you may directly run the
scripts in `crossval/trainers/`. For example:

```{bash}
python -m nullprompt.trainers.continuous_mlm [SEE --help FOR OPTIONS]
```

### On Your Own Data

Our codebase should work "out-of-the-box" on many common data formats (e.g.,
csv, tsv, jsonl), provided the input and output fields do not need to be
modified. To construct prompts we use the same template-based approach as the
[`ucinlp/autoprompt`](https://github.com/ucinlp/autoprompt) codebase. An
example prompt for SST-2 might look like:

`[T] {sentence} [T] [T] [P] .`

Where `[T]` denotes prompt tokens that are learned, `{sentence}` is a
placeholder for the `sentence` field, and `[P]` denotes the placement of the
`[MASK]` token used for prediction. Note that unlike in the `ucinlp/autoprompt`
codebase, special tokens such as `<s>` and `</s>` no longer need to be manually
added.

In some cases, additional preprocessing may need to be applied to prepare data
before being fed into a template. For example, a single instance might need to
be turned into many prompts (e.g., for multirc). In this case, you may need to
write a custom preprocessing function. Refer to the functions in
`nullprompt/preprocessors.py` for example.


## Citation

If you use this codebase in your own research, please cite:
```{latex}
@misc{logan2021cutting,
      title={Cutting Down on Prompts and Parameters: Simple Few-Shot Learning with Language Models}, 
      author={Robert L. Logan IV and Ivana Balažević and Eric Wallace and Fabio Petroni and Sameer Singh and Sebastian Riedel},
      year={2021},
      eprint={2106.13353},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
