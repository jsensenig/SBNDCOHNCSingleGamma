#ifndef _sbnumurecodata_TruthMatch_hh
#define _sbnumurecodata_TruthMatch_hh

#include "TVector3.h"

#include "ana/SBNOscReco/Data/Mode.h"

namespace numu {
/**
* Matching information between a Track and truth
*/
struct TrackTruthMatch {
  bool has_match; //!< Whether a track match exists
  bool mctruth_has_neutrino; //!< Whether the MCTruth object this track matches to is a neutrino interaction
  TVector3 mctruth_vertex; //!< The interaction vertex of the MCTruth object this track matches to
  int mctruth_origin; //!< Value of Origin_t enum of the MCTruth object this track matches to
  int mctruth_ccnc; //!< CC (1) / NC (0) value of the MCTruth this object matches to
  int mcparticle_id; //!< MCParticle ID of the particle this track matches to (same as the ID of the RecoTrack of that particle.)
  float completion; //!< Fraction of energy deposits by true particle matched by this track
  int match_pdg; //!< PDG of the MCParticle this track matches to
  bool is_primary; //!< Whether this track was produced as the "primary" process
  TrackTruthMatch():
    has_match(false),
    mctruth_has_neutrino(false),
    mctruth_vertex(-1, -1, -1),
    mctruth_origin(-1),
    mctruth_ccnc(-1),
    mcparticle_id(-1),
    completion(-1),
    match_pdg(-1),
    is_primary(false) {}
};

/**
* Matching information between a candidate neutrino interaction and truth
*/
struct TruthMatch {
  bool has_match; //!< Whether a truth match exists
  InteractionMode mode; //!< Mode of the interaction
  TrackMode tmode; //!< Mode of the primary track in this interaction
  int mctruth_vertex_id; //!< index of the truth vertex into the list of MCThruths. -1 if no match
  int mctruth_track_id; //!< index of the primary track into the list of MCTruths. -1 if no match.
  float truth_vertex_distance; //!< Distance from truth interaction vertex to this vertex
};
}
#endif
