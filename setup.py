from setuptools import setup


setup(
    name="resultify",
    version=open("VERSION", "r").read().strip(),
    description="A rust-like result type for Python",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/felixhammerl/resultify",
    author="Felix Hammerl",
    author_email="felix.hammerl@gmail.com",
    zip_safe=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="rust result",
    packages=["resultify"],
    python_requires=">=3.8",
)
