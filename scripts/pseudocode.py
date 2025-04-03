for batch_idx, train_file in enumerate(train_files):
    load current batch data and label mapping (L_t)
    if previous label mapping L_{t-1} exists:
        if L_t != L_{t-1}:
            update classifier and CRF parameters
    load model checkpoint from previous batch if available
    create DataLoader with reduced batch size
    for each epoch in fine-tuning epochs:
        for each batch in DataLoader:
            forward pass:
                compute transformer embeddings
                fuse knowledge features
                run BiLSTM and compute classifier scores
                compute CRF loss
            backward pass:
                update model parameters using AdamW
        clear GPU memory cache
    save updated model checkpoint and optimizer state
    