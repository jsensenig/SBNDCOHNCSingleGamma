#ifndef _sbnnumu_Profile_h__
#define _sbnnumu_Profile_h__

#include "HistoList.h"
#include "../Data/RecoEvent.h"

class TH2D;
class TH3D;

namespace ana {
 namespace SBNOsc {

struct TrackProfiles : public HistoList {
  TH3D *range_minus_true;
  TH3D *range_v_true_mom;
  TH3D *mcs_minus_true;
  TH3D *mcs_v_true_mom;
  TH3D *pid_confusion_tr;

  void Initialize(const std::string &postfix, unsigned nbinsx, double xlo, double xhi);
  void Fill(float val, const numu::RecoTrack &track, const numu::RecoEvent &event);   
};
  }
}

#endif
