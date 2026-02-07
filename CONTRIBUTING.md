# Contributing to Brain Robot Controller

Thank you for your interest in contributing to the Brain Robot Controller project!

## Development Setup

1. Fork and clone the repository
2. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

## Running Tests

Before submitting a pull request, ensure all tests pass:

```bash
pytest
```

## Code Style

We use:
- **Black** for code formatting
- **Flake8** for linting
- **MyPy** for type checking

Format your code before committing:

```bash
black brain_robot_controller tests examples
flake8 brain_robot_controller tests examples
mypy brain_robot_controller
```

## Pull Request Process

1. Update tests for any new functionality
2. Update documentation as needed
3. Ensure all tests pass
4. Update the README if needed
5. Submit your pull request with a clear description

## Questions?

Feel free to open an issue for any questions or discussions!
