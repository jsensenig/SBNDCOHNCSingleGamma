# Declare libraries to build
# Note that the library names (the first argument) should follow the convention
# "sbnanalysis_ThisAnalysis_LibraryName)". Libraries can be built from multiple
# source files.
add_library(sbnanalysis_SBNOscReco_TriggerEmulator SHARED PMTTrigger.cc)

target_link_libraries(sbnanalysis_SBNOscReco_TriggerEmulator
  sbndcode_OpDetSim
  sbnanalysis_SBNOscReco_classes
)

# Install all libraries to the main "lib" directory
install(TARGETS sbnanalysis_SBNOscReco_TriggerEmulator DESTINATION lib)


