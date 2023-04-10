python3.8 examples/entity_disambiguation/evaluate.py \
  --model-dir=examples/entity_disambiguation/luke_ed_large/ \
  --dataset-dir=examples/entity_disambiguation/entity_disambiguation/ \
  --titles-file=examples/entity_disambiguation/entity_disambiguation/enwiki_20181220_titles.txt \
  --redirects-file=examples/entity_disambiguation/entity_disambiguation/enwiki_20181220_redirects.tsv \
  --inference-mode=global \
  --document-split-mode=per_mention \
  --test-set=wikipedia
