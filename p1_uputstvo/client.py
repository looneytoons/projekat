# -*- coding: utf-8 -*-

from __future__ import print_function
import urllib
import os

class SCClient:
    
    def __init__(self, code, indeks, ip='localhost', port=8080):
        self.server_url = 'http://' + ip + ':' + str(port) + '/'
        self.code = code
        
        self.train_img_suffix = '_train.jpg'
        self.test_img_suffix = '_test.jpg'
        self.request_param_indeks = '?indeks=' + indeks
    
        self.train_img = code + self.train_img_suffix
        self.test_img = code + self.test_img_suffix
        
        self.train_img_remote = self.server_url + self.train_img + self.request_param_indeks
        self.test_img_remote = self.server_url + self.test_img + self.request_param_indeks
        
        self.save_dir = os.getcwd() + '/'
        self.train_img_local = self.save_dir + self.train_img
        self.test_img_local = self.save_dir + self.test_img
        
    def download_imgs(self):
        urlopener = urllib.URLopener()
        
        urlopener.retrieve(self.train_img_remote, filename=self.train_img_local)
        print('Train image downloaded to:', self.train_img_local)
        
        urlopener.retrieve(self.test_img_remote, filename=self.test_img_local)
        print('Test image downloaded to:', self.test_img_local)
        
    def close(self):
        os.remove(self.train_img_local)
        os.remove(self.test_img_local)
        print('Client closed')