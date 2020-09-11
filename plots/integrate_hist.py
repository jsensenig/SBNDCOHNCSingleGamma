import ROOT
import util
import argparse


def main(args):
    f = ROOT.TFile(args.input)
    hist = f.Get(args.hist)
    if args.range_hi is not None and args.range_lo is not None: 
        lo_bin = hist.GetXaxis().FindBin(args.range_lo)
        hi_bin = hist.GetXaxis().FindBin(args.range_hi)
        integral = hist.Integral(lo_bin, hi_bin)
    else:
        integral = hist.Integral()
    if args.ratio:
        if args.overflow:
            total = sum([hist.GetBinContent(i) for i in range(hist.GetNbinsX()+2)])
        else:
            total = hist.Integral()
        integral = integral / total
    print integral

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser = util.with_input_args(parser)
    parser.add_argument("-rl", "--range_lo", default=None, type=float)
    parser.add_argument("-rh", "--range_hi", default=None, type=float)
    parser.add_argument("-hn", "--hist", required=True)
    parser.add_argument("-r", "--ratio", action="store_true")
    parser.add_argument("-o", "--overflow", action="store_true")
    main(parser.parse_args())

