from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import torch


def generate_summary(transcript):
    """
    Description:
        This function takes the transcript and returns summary using the google pegasus model. 

    Parameters: 
        transcript

    returns: 
        summary
    """

    model_name = "google/pegasus-xsum"
    device = "cuda" if torch.cuda.is_available() else "cpu"
    tokenizer = PegasusTokenizer.from_pretrained(model_name)
    model = PegasusForConditionalGeneration.from_pretrained(model_name).to(device)
    batch = tokenizer(transcript, truncation=True, padding="longest", return_tensors="pt").to(device)

    # Generating summary
    translated = model.generate(**batch)
    tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)

    return tgt_text[0]
