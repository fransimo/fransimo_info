function convert_2_pdf() {

  sed '1{/^---$/!q;};1,/^---$/d' $1 > tmp.md

  rm $2.pdf
  rm $2.docx

  pandoc tmp.md  -f gfm -t pdf -o $2.pdf  \
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

    pandoc tmp.md  -f gfm -t docx -o $2.docx  \
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

convert_2_pdf "_index.es.md" "fransimo_detailed_cv.es"

convert_2_pdf "_index.md" "fransimo_detailed_cv"