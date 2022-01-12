from parser import build_parser
from chain import *


if __name__ == '__main__':

    p = build_parser()

    sample_conv = SampleConvertHandler()
    haps_conv = HapsConvertHandler()
    ilash_run = ILASHHandler()
    dist_conv = DistConvertHandler()
    qc_run = QcHandler()
    graph_compiler = GraphHandler()
    infomap_handler = InfoMapHandler()
    shapeit_handler = ShapeItHandler()

    sample_conv.set_next(haps_conv)
    haps_conv.set_next(ilash_run)
    ilash_run.set_next(dist_conv)
    dist_conv.set_next(qc_run)
    qc_run.set_next(graph_compiler)
    graph_compiler.set_next(infomap_handler)
    infomap_handler.set_next(shapeit_handler)

    args = p.parse_args()
    sample_conv.handle(args)
