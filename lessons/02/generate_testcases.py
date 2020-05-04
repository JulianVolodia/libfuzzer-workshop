#!/usr/bin/env python2
import os
import random
import multiprocessing as mp

WORK_DIR = 'work'

# Create work `directory` and `corpus` subdirectory.
if not os.path.exists(WORK_DIR):
  os.mkdir(WORK_DIR)

corpus_dir = os.path.join(WORK_DIR, 'corpus')
if not os.path.exists(corpus_dir):
  os.mkdir(corpus_dir)

seed_corpus_filenames = os.listdir('seed_corpus')

def gen_test(i):
  random_seed_filename = random.choice(seed_corpus_filenames)
  random_seed_filename = os.path.join('seed_corpus', random_seed_filename)
  output_filename = os.path.join(WORK_DIR, 'corpus', 'testcase-%06d' % i)
  cmd = 'bin/radamsa "%s" > "%s"' % (random_seed_filename, output_filename)
  os.popen(cmd)

pool = mp.Pool(mp.cpu_count())

results = pool.map( gen_test, [i for i in xrange(1000)])

pool.close()

