cd ./models/transformer-cnn

cell_line_list="786-0 A498 A549_ATCC ACHN BT-549 CAKI-1 CCRF-CEM COLO_205 DU-145 EKVX HCC-2998 HCT-116 HCT-15 HL-60(TB) HOP-62 HOP-92 HS_578T HT29 IGROV1 K-562 KM12 LOX_IMVI M14 MALME-3M MCF7 MDA-MB-231_ATCC MDA-MB-435 MDA-N MOLT-4 NCI-H226 NCI-H23 NCI-H322M NCI-H460 NCI-H522 NCI_ADR-RES OVCAR-3 OVCAR-4 OVCAR-5 OVCAR-8 PC-3 RPMI-8226 RXF_393 SF-268 SF-295 SF-539 SK-MEL-2 SK-MEL-28 SK-MEL-5 SK-OV-3 SN12C SNB-19 SNB-75 SR SW-620 T-47D TK-10 U251 UACC-257 UACC-62 UO-31"
splits="umap scaffold random butina"

idx=0
for seed in {1..5};do    
    for split in $splits; do
        for cell_line in $cell_line_list;do
            for fold in {1..7};do
                idx=$((idx+1))
                if [[ $idx -eq $PBS_ARRAY_INDEX ]]; then
                    predictions_file="${HOME}}/UMAP_split_for_VS/results/TRANSCNN/$cell_line/fold_${fold}/seed_${seed}/split_${split}/test_predictions.csv"
                    if [[ ! -f "$predictions_file" ]]; then
                        python transformer-cnn.py configs/${cell_line}_split_${split}_fold_${fold}_seed_${seed}.cfg
                    fi
                fi
            done
        done
    done
done


