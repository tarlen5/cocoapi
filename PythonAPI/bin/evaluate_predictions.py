"""
author: Timothy C Arlen

date: 27 March 2018
"""

from argparse import ArgumentParser,ArgumentDefaultsHelpFormatter

from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval

parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument(
    'annotations', 
    type=str,
    help='Annotations JSON file in the COCO fomat')
parser.add_argument(
    'predictions',
    type=str,
    help='Predictions (results) file in the COCO format')
parser.add_argument(
    '--cat_idx',
    type=int,
    default=None,
    required=False,
    help='category index of COCO dataset to evaluate (default "None" val is all)')
args = parser.parse_args()

ann_type = "bbox" # Only type supported for now

coco_gt = COCO(args.annotations, use_single_cat=args.cat_idx)
coco_dt = coco_gt.loadRes(args.predictions)
coco_eval = COCOeval(coco_gt, coco_dt, ann_type)

coco_eval.evaluate()
coco_eval.accumulate()
coco_eval.summarize()
