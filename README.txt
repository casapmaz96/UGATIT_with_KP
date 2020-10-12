### RUNNING UGATIT ###

IMPORTANT:
	-Please unzip sapmaz-furdui_dataset.zip into this directory 705. Its name should be dataset.
	-Please unzip the saved model parameters as follows:
	Unzip the following into KPEP32040/celebKP/model 
	https://cityuni-my.sharepoint.com/:u:/g/personal/cansin_sapmaz_city_ac_uk/EUWHOIF_SUlNpY2WfPFDfDQByDcojKTesk1nioOYW4HbUg?e=d10mKj

	Unzip the following into KPEP32040/celebKP/modelkp
	https://cityuni-my.sharepoint.com/:u:/g/personal/cansin_sapmaz_city_ac_uk/ERX8ZgyrSWJFv1gVyzw-YaoBOjosYh91JxP-VgPjUgWhAA?e=tUf3cv

	Unzip the following into noKP/celebKP/model
	https://cityuni-my.sharepoint.com/:u:/g/personal/cansin_sapmaz_city_ac_uk/EarakxW_p_NEvsh0fXGKra4BIusAlcK680sm2P4y8YlfzQ?e=IPWkwH

### For FID scores, please read the README file in FID_folder ###

#Scripts#

	train-withkp.sh : trains the model to 50K iterations with keypoint loss
	train-nokp.sh : trains the model to 50K iterations without keypoint loss (original UGATIT)
	test-withkp.sh : tests the model trained with keypoints
	test-nokp.sh : tests the model trained without keypoints


#Running the code manually#

You can run main.py for training or testing the model.
Please always use --light True and --dataset celebKP

	python3 main.py --light True --dataset celebKP 
		--phase : can be 'train' or 'test'
		--result_dir : directory name to print results into and/or get saved models for testing.
Please use KPEP32040 for the model trained with keypoint loss, noKP for the original UGATIT model 
		--iteration : how many times to iterate for training GAN. 
		--resume : true/false; keep training from a saved model
		If true, iteration should be the final iteration; i.e. if you trained 10K and want to train 10K more, please set --iteration 20000
		--trainkp : true/false; train the keypoint predictor beforehand or not
		--with_kp : true/false; use keypoint loss, or not. With this set to false, the code runs as the original UGATIT model.
		--kpep: integer; how many epochs to train the keypoint predictor beforehand


#Output format#
Output images and saved models can be found in the directory passed to --result_dir
img folder contains the images that result from the training
model folder contains the saved parameters of UGATIT
modelkp folder contains the saved parameters of the keypoint predictor
test folder contains the images resulting from test runs
AFID, BFID, RECFID folders contain test results as well, but unformatted/unconcatinated. 

#Dataset Format#
All datasets must be inside the dataset folder in the following format:

dataset/yourDataSetName/trainA : training human images
dataset/yourDataSetName/testA : testing human images
dataset/yourDataSetName/trainB : training anime images
dataset/yourDataSetName/testB: testing anime images
dataset/yourDataSetName/kp : keypoint annotation file of all human images
