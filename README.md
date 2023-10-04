[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](http://creativecommons.org/licenses/by/4.0/)

# Thin-film solar cell ontology

_Work in Progress!_

## Table of Contents
  * [About TFSCO](#about-tfsco)
  * [Use of TFSCO](#use-of-tfsco)
  * [Top level Ontology](#top-level-ontology)
  * [Mid- and Domain-level Ontologies](#mid--and-domain-level-ontologies)
  * [News](#news)
  * [Links](#links)
  * [Content license](#content-license)
  * [Footnotes](#footnotes)

## About TFSCO
The Thin-film solar cell ontology (TFSCO) is a domain ontology that provides a model  of the manufacturing and characterization of perovskite solar cells. The TFSCO has been under development since 2022. The OWL-File was created using [Protégé](https://protege.stanford.edu/). Protégé may be used for viewing and editing the ontology. The TFSCO classes can be viewed via the MatPortal.org (Link below).

## Use of TFSCO
Efforts have been made to implement a Nomad<sup>1</sup> database/structure that enables a linkage between the ontology classes and the research data stored via the IRI. This secures a sustainable and machine readable data structure based on the of the ontology and a user friendly interface with quality of life features like filters, plots and histograms from Nomad.

## Upper-level Ontologies
The TFSCO uses the Basic Formal Ontology ([BFO](https://github.com/BFO-ontology/BFO)) as its Top-Level Ontology. A selection of relations have been imported from the [RO](http://obofoundry.org/ontology/ro.html) (Relation Ontology).

## Mid- and Domain-level Ontologies
The TFSCO imports axioms from the following ontologies: [CHMO](https://github.com/rsc-ontologies/rsc-cmo) (Chemical Methods Ontology), [PATO](http://obofoundry.org/ontology/pato.html) (Phenotype and trait ontology), [CHEBI ](https://www.ebi.ac.uk/ols/ontologies/chebi) (Chemical entities of biological interest), [IAO](https://github.com/information-artifact-ontology/IAO) (Information Artifact ontology).
## News
-09/22/2022 The first version of peroman was initialised by AK. <br>
-07/03/2023 Peroman was split up into the TFSCO and...

## Links

- [GitHub](https://github.com/RoteKekse/autoperosol)
- [TFSCO on MatPortal.org Repository](https://matportal.org/ontologies/TFSCO)

### Content license: 
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.en)


### Footnotes
<sup>1</sup> "[NOMAD](https://nomad-lab.eu/nomad-lab/) is a free web-service that lets you share your data or use comprehensive
data that others provide. You can use NOMAD to organize, analyze, share, 
and publish your materials science data, as well as explore, download, 
and analyze your colleagues' data." (Nomad. Retrieved from: https://nomad-lab.eu/nomad-lab/index.html Retrieved on: 07/13/23)
