#!/bin/bash
cat access.log |
  awk '{tms[$12]++;next}END{for (t in tms) print t, tms[t]}'
