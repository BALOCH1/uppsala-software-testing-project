all: exe_ab exe_fb exe_fw exe_hb exe_hw exe_hsb exe_mb exe_mw exe_mzb

exe_ab: Arslan_test/BlackBox_Test.py
	python3 Arslan_test/BlackBox_Test.py

exe_fb: felix_tests/blackbox_test_pandas.py
	python3	felix_tests/blackbox_test_pandas.py

exe_fw: felix_tests/whitebox_test_pandas.py
	python3	felix_tests/whitebox_test_pandas.py

exe_hb: Henrik_tests/BlackBoxTesting.py
	python3	Henrik_tests/BlackBoxTesting.py

exe_hw: Henrik_tests/WhiteBoxTesting.py
	python3	Henrik_tests/WhiteBoxTesting.py

exe_hsb: Hassnain_tests/BlackBox_Testing.py
	python3	Hassnain_tests/BlackBox_Testing.py

exe_mb: maria_tests/blackBoxtesting.py 
	python3 maria_tests/blackBoxtesting.py

exe_mw: maria_tests/whiteboxtesting.py 
	python3 maria_tests/whiteboxtesting.py

exe_mzb: Muzammil_test/blackboxtesting.py 
	python3 Muzammil_test/blackboxtesting.py

