import ROOT
import util
import argparse


def main(args):
    hists = [[util.get_tobject(args, h.lstrip("-")) for h in hlist] for hlist in args.hstack]
    util.validate_hists(args.hstack, hists)
    hists = [[util.resize_histo(args, h) for h in hlist] for hlist in hists]

    canvas = ROOT.TCanvas("canvas", "Canvas", 250,100,700,500)
    hstack = ROOT.THStack()

    for i, (hlist,hnames) in enumerate(zip(hists, args.hstack)):
        h = hlist[0]
        if len(hlist) > 1:
            for hadd,hname in zip(hlist[1:],hnames[1:]):
                #if "InTime-" in hname:
                #   h.Add(hadd, 10. / 1837.)
                if hname.startswith("-"):
                    h.Add(hadd, -1)
                else:
                    h.Add(hadd)
  
        if args.area_normalize and h.Integral() > 1e-4: h.Scale(1. / h.Integral())
        color = util.namecolors(args.names[i] if args.names else hnames[0])
        if args.stack:
            h.SetFillColor(color)
        else:
            h.SetLineColor(color)
            h.SetLineWidth(3)
        if args.names: 
            name = args.names[i]
            if args.nevent_in_legend:
                name += " (%i)" % int(h.Integral()) 
            h.SetTitle(name)
        hstack.Add(h)

    drawstr = "HIST" if args.stack else "NOSTACK HIST"
    hstack.Draw(drawstr)
    util.style(args, canvas, hstack)
    if args.legend_position: legend = ROOT.gPad.BuildLegend(*(args.legend_position + [""]))
    if args.logy:
        canvas.SetLogy()

    box = util.draw_text(args)
    canvas.Update()

    util.wait(args)
    util.write(args, canvas)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser = util.with_io_args(parser)
    parser = util.with_histosize_args(parser)
    parser = util.with_histostyle_args(parser)
    parser = util.with_text_args(parser)
    parser.add_argument("-ly", "--logy", action="store_true")
    parser.add_argument("-hs", "--hstack", required=True, type=util.histo_list)
    parser.add_argument("-s", "--stack", action="store_true")
    parser.add_argument("-n", "--names", default=None, type=util.comma_separated)
    parser.add_argument("-a", "--area_normalize", action="store_true")
    parser.add_argument("--nevent_in_legend", action="store_true")
    parser.add_argument("-lp", "--legend_position", default=None, type=util.legend_position)
    main(parser.parse_args())

