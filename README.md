# GPT4Readability

[![License Badge](https://img.shields.io/github/license/loevlie/GPT4Readability)](https://github.com/loevlie/GPT4Readability/blob/main/LICENSE)
[![Issues Badge](https://img.shields.io/github/issues/loevlie/GPT4Readability)](https://github.com/loevlie/GPT4Readability/issues)
[![Pull Requests Badge](https://img.shields.io/github/issues-pr/loevlie/GPT4Readability)](https://github.com/loevlie/GPT4Readability/pulls)
[![Contributors Badge](https://img.shields.io/github/contributors/loevlie/GPT4Readability)](https://github.com/loevlie/GPT4Readability/graphs/contributors)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)

GPT4Readability is a powerful tool designed to automatically generate a README.md file and suggest code improvements for any code repository. It leverages the capabilities of OpenAI's GPT-3.5-turbo or GPT-4 model to analyze and interpret code, establish connections between different parts of the codebase, and gain an in-depth understanding of its functionality, structure, and intent.

> Other than this sentence this readme file and this [suggestions file](https://github.com/loevlie/GPT4Readability/blob/main/suggestions.md) were both generated by GPT4Readability using gpt-3.5-turbo.  Any other changes made will be listed below:

* I added the version (0.0.8) to the installation section.
* UPDATE: README generation (suggestions coming soon!) is now integrated into [Huggingface Spaces 🤗](https://huggingface.co/spaces) using [Gradio](https://github.com/gradio-app/gradio). Try out the Web Demo: [![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/JohanDL/GPT4Readability)
* I recently got access to GPT-4 so the GPT-4 version of the gpt4readability README can be found here [GPT-4_Example](https://github.com/loevlie/GPT4Readability/blob/main/Example_READMEs/gpt4readability_gpt4_readme.md)
* The README file generation works with all programing languages but for now the code suggestions is still python only. 

## Features

- Automatic generation of a comprehensive README.md file for your codebase
- Suggestions for code improvements to enhance readability and maintainability

## Installation

To use GPT4Readability, you need to have Python 3.6 or higher installed on your system. You can install GPT4Readability and its dependencies using the following command:

```shell
pip install GPT4Readability==0.0.8
```

## Usage

GPT4Readability provides a command-line interface (CLI) for generating the README.md file and code improvement suggestions. You can use the following command to run GPT4Readability:

```shell
gpt4readability [path] [options]
```

### Options

- `--function`, `-f`: Specify the function to use. Options are 'readme', 'suggestions', or 'both'. Default is 'both'.
- `--output_readme`, `-or`: Specify the output filename for the README.md file. Default is 'README.md'.
- `--output_suggestions`, `-os`: Specify the output filename for the code improvement suggestions. Default is 'suggestions.md'.
- `--model`, `-m`: Specify the model to use. Options are 'gpt-3.5-turbo' or 'gpt-4'. Default is 'gpt-3.5-turbo'.

### Examples

To generate the README.md file for your codebase, run the following command:

```shell
gpt4readability /path/to/codebase --function readme
```

To generate code improvement suggestions for your codebase, run the following command:

```shell
gpt4readability /path/to/codebase --function suggestions
```

To generate both the README.md file and code improvement suggestions, run the following command:

```shell
gpt4readability /path/to/codebase --function both
```

## Authors

GPT4Readability is developed and maintained by Dennis Johan Loevlie. You can contact the author via email at loevliedenny@gmail.com.

## Contributing

Contributions to GPT4Readability are welcome! If you encounter any issues or have suggestions for improvements, please open an issue on the [GitHub repository](https://github.com/loevlie/GPT4Readability/issues). 

## Support

If you need support or have any questions, feel free to reach out to the author at loevliedenny@gmail.com.

## License

GPT4Readability is licensed under the [MIT License](https://github.com/loevlie/GPT4Readability/blob/main/LICENSE).
