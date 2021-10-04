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

#### A Note on Config Names

The config names are comprised of a sequence of underscore delimited field.
Each config starts with the name of the task, e.g., `boolq`, `cb`, etc.
The next field is the model the config is for, either: `roberta` or `albert`.

Afterwards comes `initial-trigger` which is either: `true` or `false`.
This field specifies whether or not trigger tokens in the prompt are
manually initialized, and is only useful for models that have some kind of
learned prompt.

Finally there is the `finetune-mode` field, which describes which parameters
are finetuned, the options are:
- `adapter`: Adapter layers are added to the model and only the adapter weights
  are tuned.
- `all`: All parameters are tuned.
- `bitfit`: Bias terms are tuned.
- `calibration`: A calibration layer is added on top of the lm head, and its
  weights are tuned. 
- `discrete`: The prompt tokens are tuned using the approach described in the [AutoPrompt](https://arxiv.org/abs/2010.15980) paper.
- `layernorm`: Bias terms and layernorm parameters are tuned.
- `partial`: Trigger weights and the lm head weights are tuned.
- `triggers`: Only the embeddings of the prompt tokens are tuned.
Note that in some cases we experiment with combining some of these settings, in
which case they are joined with a `+` sign (e.g., `bitfit+triggers`).

Any remaining text provides additional description of the experiment setting.
Notably: 
- `no-trigger`: means that a *Null Prompt* was used,
- `random-labels`: means that a *Null Verbalizer* was used, and 
- `n-token` means that `n` trigger tokens were prepended to the prompt.


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
