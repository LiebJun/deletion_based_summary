import argparse
# from transformers.models.auto.configuration_auto import AutoConfig
# from utils import init_logger, set_seed, init_system

import torch
from utils import *

from trainer import train

from summary_model import DeletionBasedSummaryModel

device = 'cuda' if torch.cuda.is_available() else 'cpu'


def main(cli_args):
    
    args = init_setting(cli_args)
    model = DeletionBasedSummaryModel(args).to(device)

    if args.do_train:
        train(args, model)
    print(" Debugging is done")
    # if args.do_train:
    #     ### Training configs ###
    #     ### Data Loading ###
    #     global_step, train_loss = train(args, train_dataloader, model, tokenizer, test_dataloader)
    #     logger.info(" global_step = %s, average loss = %s", global_step, train_loss)

    # if args.do_eval:
    #     best_acc = 0
    #     best_checkpoint = ''
    #     checkpoints = sorted([_ for _ in os.listdir(args.output_dir) if _.startswith('best')])
    #     logger.info(f"Evaluate the following checkpoint: {args.output_dir}")

    #     for checkpoint in checkpoints:
    #         global_step = checkpoint.split("-")[-1]
    #         model = torch.load(os.path.join(args.output_dir, checkpoint, 'intent_class_model.pt'))
    #         tokenizer = AutoTokenizer.from_pretrained(os.path.join(args.output_dir, checkpoint))
            
    #         eval_loss, eval_acc = evaluate(args, model, tokenizer, test_dataloader)
            
    #         if eval_acc > best_acc:
    #             best_acc = eval_acc
    #             best_checkpoint = checkpoint
    #         # result.append(f'[{checkpoint}] Loss: {eval_loss:.3f}, Accuaracy: {eval_acc:.3f}')
    #         logger.info(f'[{checkpoint}] Loss: {eval_loss:.4f}, Accuaracy: {eval_acc:.4f}')
    #     logger.info(f"[VALID] All checkpoint validations are done.")
    #     logger.info(f"Best checkpoint: {best_checkpoint}, Accuracy: {best_acc:.2f}")
        
    # logger.info(f"finished")
    # train_logger.info('finished')

    

if __name__ == '__main__':
    cli_parser = argparse.ArgumentParser()
    cli_parser.add_argument("--config_file", type=str, default='koelectra_small.json')
    cli_parser.add_argument("--output_dir", type=str, default='koelectra_small_ckpt')
    cli_args = cli_parser.parse_args()

    main(cli_args)
