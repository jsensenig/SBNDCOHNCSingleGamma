#ifndef _sbnumurecodata_Mode_hh
#define _sbnumurecodata_Mode_hh

namespace numu {
/**
* Enum to hold each different typoe of reconstructed event
*/
enum InteractionMode {
  mCC = 0,  
  mCCNonPrimary = 1,
  mNC = 2, 
  mNCNonPrimary = 3,
  mCosmic = 4, 
  mIntimeCosmic = 5,
  mOther = 6,
  mAll = 7
};

/**
 * Enum to hold different types of tracks.
 */
enum TrackMode {
  tmOther = -1,
  tmCosmic = 1,
  tmNeutrino = 2
};
}
#endif
