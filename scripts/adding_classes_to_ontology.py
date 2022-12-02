#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 09:45:12 2022

@author: a2853
"""

from owlready2 import *

onto = get_ontology("file://../peroman.owl").load()

def _cas_search_unique(search):
    import requests
    response = requests.get(
        f'https://commonchemistry.cas.org/api/search?q={search}')
    if response.status_code == 200:
        response_dict = response.json()
        n_hits = response_dict.get("count", 0)
        if n_hits == 0:
            return None
        elif n_hits >= 1:
            try:
                cas_number = [response_dict["results"][i]["rn"] for i in range(n_hits)]
                return cas_number
            except KeyError:
                return None
        else:
            return None
    return None


def _populate_from_cas(cas_number):
    '''Private method for populating the attributes from a call to the CAS API using
    the `cas_number`.
    Will overwrite exisiting CAS attributes if the query provides a value for them.
    I.e. all attributes that begin with `cas_`.

    Args:
        archive (EntryArchive): The archive that is being normalized.
        logger (Any): A structlog logger.
    '''
    import requests
    response = requests.get(
        f'https://commonchemistry.cas.org/api/detail?cas_rn={cas_number}')
    if response.status_code == 200:
        response_dict = response.json()
        return response_dict
    elif response.status_code == 404:
        print("No CAS entry found with CAS number: {self.cas_number}")
    elif response.status_code == 500:
        print("Remote server error on CAS API call.")
    else:
        print(
            f"Unexpected response code: {response.status_code} from CAS API call.")

for c in onto.classes():
    if "Solvent" in c.label:
        for inst in c.instances():
            cas = _cas_search_unique(inst.label[0])
            if cas:
                for ca in cas:
                    res = _populate_from_cas(ca)
                    print(inst.label,ca,res["name"])
                
            
            
            
            



