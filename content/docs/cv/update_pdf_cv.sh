function convert_2_pdf() {

  sed '1{/^---$/!q;};1,/^---$/d' $1 > tmp.md

  pandoc tmp.md -t docx -o tmp.docx

  rm $2

  pandoc tmp.md  -f gfm -t pdf -o $2  \
        --include-in-header pdf_prop.tex \
        -V geometry:portrait \
        -V geometry:top=2cm \
        -V geometry:right=2cm \
        -V geometry:bottom=2cm \
        -V geometry:left=2cm \
        -V geometry:a4paper \
        -V mainfont="DejaVu Serif" \
        -V monofont="DejaVu Sans Mono" \
        -V fontsize=12pt ## --toc

  rm tmp.md
}

convert_2_pdf "detailed_cv.es.md" "detailed_cv.es.pdf"