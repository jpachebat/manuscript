# PhD Manuscript

This repository contains the LaTeX source files for my PhD thesis manuscript.

## Project Structure

```
manuscript/
├── main.tex                    # Main document file
├── chapters/                   # Individual chapter files
│   ├── abstract.tex
│   ├── acknowledgments.tex
│   ├── 01_introduction.tex
│   ├── 02_literature_review.tex
│   ├── 03_methodology.tex
│   ├── 04_results.tex
│   ├── 05_discussion.tex
│   └── 06_conclusion.tex
├── appendices/                 # Appendix files
│   └── appendix_a.tex
├── bibliography/               # Bibliography files
│   └── references.bib
├── figures/                    # Figure files (PDF, PNG, JPG, etc.)
├── tables/                     # Table data files (if separate)
├── MANUSCRIPT_PLAN.md          # Planning and progress tracking
└── README.md                   # This file
```

## Prerequisites

You need a LaTeX distribution installed on your system:

### macOS
```bash
# Using Homebrew
brew install --cask mactex

# Or download from: https://www.tug.org/mactex/
```

### Linux (Ubuntu/Debian)
```bash
sudo apt-get update
sudo apt-get install texlive-full
```

### Windows
Download and install MiKTeX from: https://miktex.org/download

### Required Packages
The main document uses the following LaTeX packages (usually included in full distributions):
- geometry (page layout)
- inputenc, fontenc, babel (encoding and language)
- graphicx, float, subcaption (figures)
- booktabs, multirow, longtable (tables)
- amsmath, amssymb, amsthm (mathematics)
- biblatex with biber backend (bibliography)
- hyperref, cleveref (cross-references)
- fancyhdr (headers/footers)
- setspace (line spacing)

## Building the Document

### Method 1: Using Command Line (Recommended)

```bash
# Navigate to the project directory
cd /path/to/manuscript

# First compilation
pdflatex main.tex

# Generate bibliography
biber main

# Final compilations (needed for references and cross-refs)
pdflatex main.tex
pdflatex main.tex
```

### Method 2: Using LaTeX Workshop (VS Code)

1. Install the [LaTeX Workshop extension](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop)
2. Open `main.tex` in VS Code
3. Press `Cmd+Alt+B` (Mac) or `Ctrl+Alt+B` (Windows/Linux) to build
4. The extension will automatically run the necessary compilation steps

### Method 3: Using Overleaf

1. Create a new project on [Overleaf](https://www.overleaf.com/)
2. Upload all files maintaining the folder structure
3. Set the main document to `main.tex`
4. Click "Recompile"

## Build Output

After successful compilation, you'll find:
- `main.pdf` - Your compiled thesis
- `main.bbl` - Processed bibliography
- Various auxiliary files (`.aux`, `.log`, `.toc`, `.lof`, `.lot`, `.out`, `.bcf`, `.run.xml`)

## Customizing the Document

### Update Title Page Information

Edit the following in `main.tex` (around lines 55-61):

```latex
\title{Title of Your PhD Manuscript}
\author{Your Name}
\date{\today}

\newcommand{\university}{Your University Name}
\newcommand{\department}{Your Department}
\newcommand{\supervisor}{Supervisor Name}
\newcommand{\degree}{Doctor of Philosophy}
```

### Adding Figures

1. Place your figure files in the `figures/` directory
2. Reference them in your chapter files:

```latex
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.8\textwidth]{figures/your_figure.pdf}
    \caption{Your caption here}
    \label{fig:your_label}
\end{figure}
```

3. Reference in text: `As shown in Figure~\ref{fig:your_label}...`

### Adding Tables

```latex
\begin{table}[htbp]
    \centering
    \caption{Your table caption}
    \label{tab:your_label}
    \begin{tabular}{lcc}
        \toprule
        Column 1 & Column 2 & Column 3 \\
        \midrule
        Data 1 & Data 2 & Data 3 \\
        Data 4 & Data 5 & Data 6 \\
        \bottomrule
    \end{tabular}
\end{table}
```

### Adding Citations

1. Add entries to `bibliography/references.bib`:

```bibtex
@article{smith2023,
    author = {Smith, John and Doe, Jane},
    title = {An Important Paper},
    journal = {Journal Name},
    year = {2023},
    volume = {10},
    pages = {123-145}
}
```

2. Cite in text:
   - `\cite{smith2023}` → (Smith and Doe, 2023)
   - `\textcite{smith2023}` → Smith and Doe (2023)
   - `\parencite{smith2023}` → (Smith and Doe, 2023)

### Changing Bibliography Style

In `main.tex`, modify the biblatex options:

```latex
% Author-year style (current)
\usepackage[style=authoryear,backend=biber]{biblatex}

% Numeric style
\usepackage[style=numeric,backend=biber]{biblatex}

% IEEE style
\usepackage[style=ieee,backend=biber]{biblatex}
```

## Useful Commands

### Check Word Count

```bash
# Approximate word count (excludes LaTeX commands)
texcount main.tex -inc -incbib

# Alternative
detex main.tex | wc -w
```

### Find TODO Comments

```bash
grep -r "TODO\|FIXME\|XXX" chapters/
```

### Clean Build Files

```bash
# Remove auxiliary files
rm -f *.aux *.log *.out *.toc *.lof *.lot *.bbl *.bcf *.blg *.run.xml *.fls *.fdb_latexmk
```

### Validate Bibliography

```bash
# Check for undefined citations
grep "undefined" main.log

# Check for unused bibliography entries
biber main --tool --validate-datamodel
```

## Planning & Progress Tracking

Use `MANUSCRIPT_PLAN.md` to:
- Track your writing progress
- Manage chapter-by-chapter todos
- Record supervisor feedback
- Follow best practices
- Maintain motivation

Update it regularly to stay organized!

## Git Workflow

### Initial Setup (if not already done)

```bash
git init
git add .
git commit -m "Initial manuscript setup"
```

### Regular Workflow

```bash
# Check status
git status

# Add changes
git add chapters/01_introduction.tex

# Commit with descriptive message
git commit -m "Draft introduction background section"

# View history
git log --oneline
```

### What to Commit

**Do commit:**
- All `.tex` files
- `.bib` files
- Figure source files
- `MANUSCRIPT_PLAN.md` updates

**Don't commit:**
- `*.pdf` (except final submission)
- `*.aux`, `*.log`, `*.out`, etc.
- `*.bbl`, `*.bcf`, `*.blg`
- OS-specific files (`.DS_Store`, `Thumbs.db`)

### Recommended .gitignore

Create a `.gitignore` file:

```
# LaTeX auxiliary files
*.aux
*.lof
*.log
*.lot
*.fls
*.out
*.toc
*.fmt
*.fot
*.cb
*.cb2
.*.lb

# Bibliography auxiliary files
*.bbl
*.bcf
*.blg
*-blx.aux
*-blx.bib
*.run.xml

# Build files
*.fdb_latexmk
*.synctex.gz
*.pdfsync

# Editor files
*.swp
*~
.DS_Store
Thumbs.db

# Keep only final PDF
*.pdf
!main.pdf
```

## Troubleshooting

### "Undefined control sequence" error
- Check for typos in LaTeX commands
- Ensure all required packages are loaded
- Look at the line number in the error message

### Bibliography not appearing
- Make sure you run: `pdflatex` → `biber` → `pdflatex` → `pdflatex`
- Check that `references.bib` exists and has valid entries
- Verify `\addbibresource{bibliography/references.bib}` path is correct

### References showing as "?" or "??"
- Run `pdflatex` multiple times (usually 2-3 times)
- Check that labels match (e.g., `\label{fig:test}` and `\ref{fig:test}`)

### Package not found
```bash
# On Linux/Ubuntu
sudo apt-get install texlive-latex-extra texlive-fonts-extra

# On macOS with MacTeX, packages should be included
# On Windows with MiKTeX, it will prompt to install missing packages
```

### File not found (graphics)
- Check file path and extension
- Ensure figures are in the `figures/` directory
- Use forward slashes: `figures/image.pdf` (not backslashes)

## Resources

### LaTeX Help
- [Overleaf Documentation](https://www.overleaf.com/learn)
- [LaTeX Wikibook](https://en.wikibooks.org/wiki/LaTeX)
- [TeX Stack Exchange](https://tex.stackexchange.com/)

### Writing Resources
- See the **Best Practices** section in `MANUSCRIPT_PLAN.md`
- [How to Write a Thesis](https://www.ece.ucdavis.edu/~jowens/commonerrors.html)
- [The Elements of Style](https://www.amazon.com/Elements-Style-Fourth-William-Strunk/dp/020530902X)

### Reference Management
- [Zotero](https://www.zotero.org/) - Free, open-source
- [Mendeley](https://www.mendeley.com/) - Free with sync
- [JabRef](https://www.jabref.org/) - BibTeX-specific, open-source

## License

This manuscript is private and for academic purposes only.

## Contact

**Author:** [Your Name]
**Email:** [your.email@university.edu]
**Supervisor:** [Supervisor Name]
**Institution:** [Your University]

---

**Last Updated:** October 29, 2025
