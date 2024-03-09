import glob
import os
import time

from libjpx import JPXXbrlPath,XBRLLinkBaseTree,XBRLInstanceFileAnalysis

import logging
from logging import StreamHandler, FileHandler, Formatter
from logging import INFO, DEBUG, NOTSET


#ログの設定
stream_handler = StreamHandler()
stream_handler.setLevel(DEBUG)
#stream_handler.setFormatter(Formatter("%(asctime)s - %(levelname)s:%(name)s - %(message)s"))
stream_handler.setFormatter(Formatter("%(asctime)s@ %(name)s [%(levelname)s] %(funcName)s: %(message)s"))

if not os.path.exists('.' + os.sep + 'log') :
	os.makedirs('.' + os.sep + 'log')

datetime_str = time.strftime('%Y%m%d%H%M%S', time.localtime())
log_file_path = '.' + os.sep + 'log' + os.sep + 'tdnet_xbrl_test_' + datetime_str + '.log'
file_handler = FileHandler(log_file_path, encoding='utf-8')
#file_handler.setFormatter(Formatter("%(asctime)s - %(levelname)s:%(name)s - %(message)s"))
file_handler.setFormatter(Formatter("%(asctime)s@ %(name)s [%(levelname)s] %(funcName)s: %(message)s"))
file_handler.setLevel(DEBUG)

logging.basicConfig(level=NOTSET, handlers = [stream_handler, file_handler]) 

#XBRLのパスを生成
xbrl_dir_path = 'C:\\Users\\QUWE\\Desktop\\081220240214536030\XBRLData\\Summary'
xbrl_path_data = JPXXbrlPath(xbrl_dir_path)


#定義リンクベースを読み込む
def_tree = XBRLLinkBaseTree('definition', xbrl_path_data)

#インラインXBRLを読み込む
xbrlInstanceFileData = XBRLInstanceFileAnalysis(xbrl_path_data)

#スキーマファイルおよび名称リンクベースファイルを読み込む
def_tree.read_xsd_file('RoleQuarterlyForecasts')
def_tree.read_jp_lab_file('RoleQuarterlyForecasts')

#ディメンションを指定し、値を読み込む
selected_axis_member_dict = {'tse-ed-t_ConsolidatedNonconsolidatedAxis':'tse-ed-t_NonConsolidatedMember', 'tse-ed-t_ResultForecastAxis':'tse-ed-t_ForecastMember'}
def_tree.read_instance_data('RoleQuarterlyForecasts', xbrlInstanceFileData, selected_axis_member_dict, 'CurrentYear', 'Prior1Year')

#結果の表示
def_tree.show_tree('RoleQuarterlyForecasts')

