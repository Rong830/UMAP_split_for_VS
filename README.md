# UMAP-clustering split for rigorous evaluation of AI models for virtual screening on cancer cell lines

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![PyPI version](https://badge.fury.io/py/pypi.svg)](https://badge.fury.io/py/pypi)

This repo contains all the codes used in the paper: UMAP-based clustering split for rigorous evaluation of AI models for virtual screening on cancer cell lines, using traditional machine learning models and deep learning models to illustrate the limitation of using Scaffold Splits in Drug Discovery. This repo can help researchers to reproduce what has been done in the article.
![Figure](https://github.com/ScaffoldSplitsOverestimateVS/ScaffoldSplitsOverestimateVS/assets/162518242/2fb2cd9a-5273-4dca-9072-52ac8a12312a)

## ChEMBL Shared Targets Correlation
Random and scaffold splits both risk overestimating virtual screening (VS) performance. While random splits mix structurally similar compounds across folds, scaffold splits—despite excluding shared Murcko scaffolds—can still place nearly identical molecules in different folds. For example, Vorinostat and Pyroxamide have different scaffolds but show 0.938 Pearson correlation in bioactivity across shared targets in ChEMBL v33. Such cases inflate performance by allowing models to exploit hidden similarities. For realistic evaluation, we recommend UMAP-based clustering, which better captures global structural diversity and distributional shifts in real-world VS tasks.

## Introduction to the Splits
To ensure robust and comprehensive validation of our models, we employed four distinct clustering methodologies for creating 7-fold cross-validation splits.

- `Random Split`: Randomly distributing compounds into different folds, and each fold is likely to have a representative mix of the overall dataset's characteristics. Random splits are beneficial for generalizing model performance but may inadvertently group structurally similar compounds into the same fold.
- `Scaffold Split`: Scaffold Splitting is based on the chemical scaffolds of the molecules. This method groups compounds according to their core structures, and molecules with similar scaffolds are in the same fold.
- `Butina Split`: The Butina Split uses the Butina clustering algorithm, which is a distance-based method that groups compounds into clusters based on their chemical similarity, determined by a predefined distance threshold. This approach ensures that compounds within the same cluster (and thus the same fold) are more chemically similar to each other than to those in other clusters.
- `UMAP-based Clustering Split`: UMAP-based Clustering employs Uniform Manifold Approximation and Projection (UMAP) for dimensionality reduction followed by clustering. This technique is used to create folds based on the reduced dimensional representation of the data, capturing intrinsic patterns and structures that might not be apparent in the original high-dimensional space.

Each of these clustering methods has been utilized to create distinct sets of folds in our dataset, enabling us to thoroughly evaluate our models' capabilities and limitations across diverse chemical data landscapes.

## Installation
These instructions will guide you through setting up the Conda environment for the project.

### Prerequisites
Make sure you have Conda installed on your system. If not, you can download and install it from [here](https://www.anaconda.com/download).

### Clone the Repository
Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/Rong830/UMAP_split_for_VS.git
cd UMAP_split_for_VS
```

### Set Up Conda Environment
Create a Conda environment using the provided `requirements.txt` file. Run the following commands in the project root:

```bash
conda create --name my_environment
conda activate my_environment
conda install --file requirements.txt
```

### Download and Extract the data
All the data are available on Zenodo [here](https://zenodo.org/records/14736486)

First, download the data [here](https://zenodo.org/records/14736486/files/60_cell_lines.zip?download=1) and move the file `60_cell_lines.zip` to the `data` folder (it should be `./data/60_cell_lines.zip`).
Then, extract the drug response data for all 60 cell lines in the `data` folder.

```bash
cd data
unzip 60_cell_lines.zip
```

## Dataset Structure
The dataset located at `./data/clustering_id_k7.csv` (can be downloaded [here](https://zenodo.org/records/14736486/files/clustering_id_k7.csv?download=1)) is prepared for the 7-fold cross-validation using various splitting algorithms. Each row in the dataset represents a unique chemical compound from all 60 different cell line datasets.

- `NSC`: Unique identifier for the compound.
- `SMILES`: SMILES representation of the chemical compound.
- `Cluster_ID`: ID indicating the fold assignment for testing using UMAP-based clustering split for 7-fold cross-validation.
- `Scaffold_Cluster_ID`: ID indicating the fold assignment for testing using scaffold split for 7-fold cross-validation.
- `Random_Cluster_ID`: ID indicating the fold assignment for testing using random split for 7-fold cross-validation.
- `Butina_Cluster_ID`: ID indicating the fold assignment for testing using Butina split for 7-fold cross-validation.

Each `Cluster_ID` variant determines how compounds are assigned to the test sets in their respective folds, ensuring that the model is trained and validated comprehensively across diverse clustering methodologies.

## Usage/Examples

Run the Linear Regression and Random Forest models on all 60 cell lines:
```bash
bash run_sklearn.sh
```

Run the GEM models:
```bash
bash run_gem.sh
```

Run the Transformer-CNN models:
```bash
bash run_trans.sh
```
Modified the arguments to use different splitting methods (including scaffold split and UMAP split); or specified the cell line you want to run the model; or if you want to do hyperparamters tunning.

## Tables
### The RDKit functions are used to extract descriptors from molecules and their descriptions.
| Package                                 	| Function                                                                    	|
|-----------------------------------------	|-----------------------------------------------------------------------------	|
| AllChem.GetMorganFingerprintAsBitVect   	| Generate the Morgan Fingerprints for the molecules. [^1]                   	|
| rdMolDescriptors.CalcTPSA               	| Calculate the area of the total polar surface.                              	|
| rdMolDescriptors.CalcExactMolWt         	| Calculate the molecular weight.                                             	|
| rdMolDescriptors.CalcCrippenDescriptors 	| Calculate the Crippen-Wildman partition coefficient (logP) parameters [^2]. 	|
| rdMolDescriptors.CalcNumAliphaticRings  	| The number of aliphatic rings.                                              	|

[^1]: Rogers, D., Hahn, M.: Extended-Connectivity Fingerprints. J. Chem. Inf. Model. 50, 742–754 (2010). [https://doi.org/10.1021/ci100050t](https://doi.org/10.1021/ci100050t).

[^2]: Wildman, S.A., Crippen, G.M.: Prediction of physicochemical parameters by atomic contributions. Journal of Chemical Information and Computer Sciences 1999, 39 (5), 868-873. [https://doi.org/10.1021/ci990307l](https://doi.org/10.1021/ci990307l).


### Table of Splitting Size for Each Cell Line

|    Cell Line    | Total Size | Random Split |             |             |             |             |             |             | Scaffold Split |             |             |             |             |             |             | Butina Split |             |             |             |             |             |             |  UMAP Split |             |             |             |             |             |             |
|:---------------:|:----------:|:------------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:--------------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:------------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|
|                 |            | Fold 1 Size  | Fold 2 Size | Fold 3 Size | Fold 4 Size | Fold 5 Size | Fold 6 Size | Fold 7 Size | Fold 1 Size    | Fold 2 Size | Fold 3 Size | Fold 4 Size | Fold 5 Size | Fold 6 Size | Fold 7 Size | Fold 1 Size  | Fold 2 Size | Fold 3 Size | Fold 4 Size | Fold 5 Size | Fold 6 Size | Fold 7 Size | Fold 1 Size | Fold 2 Size | Fold 3 Size | Fold 4 Size | Fold 5 Size | Fold 6 Size | Fold 7 Size |
| 786-0           | 31,483     | 4,507        | 4,492       | 4,482       | 4,519       | 4,482       | 4,497       | 4,504       | 4,147          | 4,217       | 5,563       | 4,375       | 4,690       | 4,341       | 4,150       | 4,470        | 4,527       | 4,569       | 4,498       | 4,516       | 4,442       | 4,461       | 6,932       | 7,343       | 3,524       | 2,065       | 5,717       | 1,702       | 4,200       |
| A498            | 27,887     | 3,979        | 3,996       | 3,997       | 3,985       | 3,970       | 3,980       | 3,980       | 3,606          | 3,693       | 4,877       | 3,906       | 4,230       | 3,837       | 3,738       | 4,014        | 3,980       | 4,100       | 3,975       | 4,008       | 3,917       | 3,893       | 6,025       | 6,366       | 3,148       | 1,913       | 5,114       | 1,616       | 3,705       |
| A549_ATCC       | 32,080     | 4,619        | 4,579       | 4,568       | 4,589       | 4,577       | 4,578       | 4,570       | 4,231          | 4,273       | 5,665       | 4,432       | 4,833       | 4,409       | 4,237       | 4,587        | 4,603       | 4,588       | 4,560       | 4,572       | 4,591       | 4,579       | 7,057       | 7,393       | 3,629       | 2,140       | 5,851       | 1,749       | 4,261       |
| ACHN            | 31,650     | 4,548        | 4,504       | 4,501       | 4,550       | 4,494       | 4,540       | 4,513       | 4,167          | 4,226       | 5,618       | 4,380       | 4,725       | 4,378       | 4,156       | 4,493        | 4,552       | 4,576       | 4,526       | 4,513       | 4,502       | 4,488       | 6,941       | 7,342       | 3,574       | 2,108       | 5,763       | 1,693       | 4,229       |
| BT-549          | 22,162     | 3,151        | 3,148       | 3,202       | 3,158       | 3,189       | 3,154       | 3,160       | 2,896          | 2,947       | 3,809       | 3,086       | 3,373       | 3,103       | 2,948       | 3,191        | 3,239       | 3,250       | 3,143       | 3,100       | 3,157       | 3,082       | 4,918       | 5,812       | 2,373       | 1,404       | 3,595       | 1,371       | 2,689       |
| CAKI-1          | 30,144     | 4,312        | 4,306       | 4,266       | 4,334       | 4,308       | 4,341       | 4,277       | 3,974          | 4,008       | 5,293       | 4,184       | 4,543       | 4,159       | 3,983       | 4,313        | 4,351       | 4,333       | 4,315       | 4,237       | 4,303       | 4,292       | 6,577       | 7,092       | 3,321       | 1,987       | 5,502       | 1,696       | 3,969       |
| CCRF-CEM        | 30,228     | 4,337        | 4,310       | 4,326       | 4,283       | 4,344       | 4,306       | 4,322       | 3,978          | 4,044       | 5,353       | 4,193       | 4,543       | 4,125       | 3,992       | 4,330        | 4,375       | 4,306       | 4,306       | 4,324       | 4,308       | 4,279       | 6,801       | 6,931       | 3,350       | 2,032       | 5,442       | 1,675       | 3,997       |
| COLO_205        | 31,596     | 4,507        | 4,538       | 4,515       | 4,486       | 4,525       | 4,527       | 4,498       | 4,157          | 4,172       | 5,589       | 4,369       | 4,780       | 4,338       | 4,191       | 4,497        | 4,500       | 4,549       | 4,521       | 4,488       | 4,513       | 4,528       | 7,011       | 7,365       | 3,506       | 2,109       | 5,658       | 1,730       | 4,217       |
| DU-145          | 24,117     | 3,423        | 3,430       | 3,485       | 3,404       | 3,456       | 3,470       | 3,449       | 3,134          | 3,201       | 4,180       | 3,375       | 3,672       | 3,373       | 3,182       | 3,381        | 3,498       | 3,501       | 3,452       | 3,402       | 3,457       | 3,426       | 5,360       | 6,170       | 2,705       | 1,568       | 3,880       | 1,461       | 2,973       |
| EKVX            | 30,060     | 4,321        | 4,260       | 4,283       | 4,335       | 4,287       | 4,299       | 4,275       | 3,951          | 3,985       | 5,293       | 4,147       | 4,552       | 4,168       | 3,964       | 4,228        | 4,247       | 4,298       | 4,336       | 4,303       | 4,337       | 4,311       | 6,611       | 6,868       | 3,467       | 1,988       | 5,448       | 1,655       | 4,023       |
| HCC-2998        | 28,814     | 4,130        | 4,110       | 4,114       | 4,084       | 4,138       | 4,112       | 4,126       | 3,813          | 3,824       | 5,091       | 3,964       | 4,325       | 3,958       | 3,839       | 4,089        | 4,180       | 4,187       | 4,124       | 4,093       | 4,063       | 4,078       | 6,340       | 6,562       | 3,255       | 1,937       | 5,284       | 1,633       | 3,803       |
| HCT-116         | 31,712     | 4,540        | 4,528       | 4,535       | 4,532       | 4,525       | 4,535       | 4,517       | 4,178          | 4,226       | 5,627       | 4,394       | 4,762       | 4,335       | 4,190       | 4,535        | 4,516       | 4,590       | 4,514       | 4,531       | 4,524       | 4,502       | 7,002       | 7,388       | 3,569       | 2,103       | 5,710       | 1,744       | 4,196       |
| HCT-15          | 31,719     | 4,551        | 4,533       | 4,507       | 4,536       | 4,547       | 4,521       | 4,524       | 4,175          | 4,215       | 5,591       | 4,389       | 4,769       | 4,373       | 4,207       | 4,498        | 4,565       | 4,557       | 4,519       | 4,545       | 4,530       | 4,505       | 6,980       | 7,418       | 3,568       | 2,089       | 5,721       | 1,744       | 4,199       |
| HL-60(TB)       | 28,788     | 4,131        | 4,106       | 4,104       | 4,082       | 4,094       | 4,155       | 4,116       | 3,845          | 3,872       | 5,071       | 3,991       | 4,320       | 3,881       | 3,808       | 4,090        | 4,214       | 4,040       | 4,148       | 4,138       | 4,058       | 4,100       | 6,391       | 6,597       | 3,191       | 1,895       | 5,300       | 1,600       | 3,814       |
| HOP-62          | 31,147     | 4,476        | 4,463       | 4,467       | 4,449       | 4,427       | 4,427       | 4,438       | 4,118          | 4,163       | 5,505       | 4,345       | 4,669       | 4,242       | 4,105       | 4,499        | 4,487       | 4,534       | 4,422       | 4,410       | 4,381       | 4,414       | 6,896       | 7,194       | 3,492       | 2,122       | 5,619       | 1,711       | 4,113       |
| HOP-92          | 28,213     | 4,044        | 3,970       | 4,038       | 4,017       | 4,055       | 4,052       | 4,037       | 3,676          | 3,779       | 4,948       | 3,912       | 4,272       | 3,894       | 3,732       | 4,082        | 4,103       | 4,054       | 4,019       | 3,999       | 3,978       | 3,978       | 6,273       | 6,569       | 3,124       | 1,876       | 5,060       | 1,627       | 3,684       |
| HS_578T         | 22,980     | 3,306        | 3,270       | 3,303       | 3,267       | 3,277       | 3,290       | 3,267       | 2,996          | 3,045       | 3,958       | 3,221       | 3,503       | 3,211       | 3,046       | 3,297        | 3,387       | 3,374       | 3,223       | 3,255       | 3,214       | 3,230       | 5,133       | 5,849       | 2,555       | 1,488       | 3,782       | 1,396       | 2,777       |
| HT29            | 31,639     | 4,556        | 4,496       | 4,500       | 4,538       | 4,497       | 4,535       | 4,517       | 4,166          | 4,242       | 5,617       | 4,395       | 4,740       | 4,310       | 4,169       | 4,523        | 4,556       | 4,526       | 4,508       | 4,540       | 4,501       | 4,485       | 7,019       | 7,250       | 3,562       | 2,124       | 5,728       | 1,722       | 4,234       |
| IGROV1          | 31,413     | 4,477        | 4,486       | 4,489       | 4,495       | 4,485       | 4,490       | 4,491       | 4,144          | 4,186       | 5,556       | 4,354       | 4,701       | 4,315       | 4,157       | 4,488        | 4,522       | 4,498       | 4,480       | 4,470       | 4,463       | 4,492       | 6,888       | 7,281       | 3,559       | 2,121       | 5,702       | 1,748       | 4,114       |
| K-562           | 31,091     | 4,459        | 4,486       | 4,421       | 4,409       | 4,458       | 4,420       | 4,438       | 4,081          | 4,162       | 5,500       | 4,319       | 4,672       | 4,235       | 4,122       | 4,449        | 4,473       | 4,454       | 4,429       | 4,455       | 4,406       | 4,425       | 6,872       | 7,206       | 3,528       | 2,033       | 5,625       | 1,714       | 4,113       |
| KM12            | 31,672     | 4,532        | 4,507       | 4,539       | 4,539       | 4,534       | 4,505       | 4,516       | 4,203          | 4,236       | 5,607       | 4,355       | 4,760       | 4,332       | 4,179       | 4,496        | 4,530       | 4,549       | 4,543       | 4,502       | 4,528       | 4,524       | 6,972       | 7,377       | 3,478       | 2,116       | 5,772       | 1,757       | 4,200       |
| LOX_IMVI        | 30,089     | 4,316        | 4,276       | 4,286       | 4,306       | 4,297       | 4,314       | 4,294       | 3,954          | 4,024       | 5,315       | 4,192       | 4,479       | 4,136       | 3,989       | 4,297        | 4,365       | 4,280       | 4,358       | 4,281       | 4,252       | 4,256       | 6,709       | 6,870       | 3,348       | 2,052       | 5,454       | 1,660       | 3,996       |
| M14             | 31,416     | 4,495        | 4,499       | 4,498       | 4,490       | 4,470       | 4,491       | 4,473       | 4,151          | 4,187       | 5,570       | 4,370       | 4,645       | 4,340       | 4,153       | 4,430        | 4,534       | 4,529       | 4,460       | 4,474       | 4,491       | 4,498       | 6,941       | 7,267       | 3,526       | 2,035       | 5,737       | 1,693       | 4,217       |
| MALME-3M        | 29,271     | 4,215        | 4,176       | 4,185       | 4,201       | 4,190       | 4,180       | 4,124       | 3,855          | 3,936       | 5,179       | 4,035       | 4,401       | 4,038       | 3,827       | 4,237        | 4,225       | 4,191       | 4,164       | 4,161       | 4,129       | 4,164       | 6,478       | 6,727       | 3,308       | 1,957       | 5,284       | 1,584       | 3,933       |
| MCF7            | 24,264     | 3,460        | 3,443       | 3,505       | 3,428       | 3,488       | 3,468       | 3,472       | 3,184          | 3,161       | 4,169       | 3,407       | 3,710       | 3,388       | 3,245       | 3,436        | 3,513       | 3,542       | 3,490       | 3,401       | 3,451       | 3,431       | 5,401       | 6,128       | 2,769       | 1,607       | 3,900       | 1,505       | 2,954       |
| MDA-MB-231_ATCC | 23,907     | 3,397        | 3,389       | 3,455       | 3,377       | 3,432       | 3,438       | 3,419       | 3,110          | 3,169       | 4,113       | 3,348       | 3,633       | 3,353       | 3,181       | 3,411        | 3,441       | 3,531       | 3,431       | 3,361       | 3,376       | 3,356       | 5,339       | 6,121       | 2,667       | 1,534       | 3,865       | 1,460       | 2,921       |
| MDA-MB-435      | 24,347     | 3,456        | 3,455       | 3,497       | 3,454       | 3,494       | 3,505       | 3,486       | 3,167          | 3,226       | 4,163       | 3,415       | 3,711       | 3,429       | 3,236       | 3,465        | 3,503       | 3,533       | 3,516       | 3,421       | 3,460       | 3,449       | 5,392       | 6,281       | 2,737       | 1,569       | 3,922       | 1,483       | 2,963       |
| MDA-N           | 17,948     | 2,557        | 2,510       | 2,643       | 2,576       | 2,548       | 2,563       | 2,551       | 2,351          | 2,352       | 3,135       | 2,499       | 2,728       | 2,497       | 2,386       | 2,382        | 2,564       | 2,622       | 2,553       | 2,558       | 2,700       | 2,569       | 3,857       | 4,259       | 2,512       | 1,330       | 2,730       | 1,089       | 2,171       |
| MOLT-4          | 31,388     | 4,512        | 4,464       | 4,471       | 4,493       | 4,506       | 4,471       | 4,471       | 4,163          | 4,199       | 5,525       | 4,356       | 4,731       | 4,280       | 4,134       | 4,505        | 4,544       | 4,483       | 4,480       | 4,467       | 4,439       | 4,470       | 6,970       | 7,245       | 3,562       | 2,057       | 5,667       | 1,731       | 4,156       |
| NCI_ADR-RES     | 24,312     | 3,451        | 3,449       | 3,515       | 3,456       | 3,508       | 3,480       | 3,453       | 3,157          | 3,212       | 4,178       | 3,406       | 3,714       | 3,392       | 3,253       | 3,455        | 3,471       | 3,533       | 3,500       | 3,427       | 3,482       | 3,444       | 5,342       | 6,281       | 2,731       | 1,585       | 3,916       | 1,476       | 2,981       |
| NCI-H226        | 29,739     | 4,261        | 4,228       | 4,255       | 4,268       | 4,242       | 4,239       | 4,246       | 3,956          | 3,998       | 5,205       | 4,106       | 4,463       | 4,077       | 3,934       | 4,277        | 4,244       | 4,402       | 4,204       | 4,176       | 4,211       | 4,225       | 6,575       | 6,937       | 3,251       | 1,987       | 5,386       | 1,665       | 3,938       |
| NCI-H23         | 31,705     | 4,557        | 4,515       | 4,519       | 4,534       | 4,548       | 4,517       | 4,515       | 4,195          | 4,246       | 5,623       | 4,351       | 4,784       | 4,342       | 4,164       | 4,519        | 4,529       | 4,555       | 4,505       | 4,517       | 4,534       | 4,546       | 7,009       | 7,283       | 3,580       | 2,094       | 5,782       | 1,737       | 4,220       |
| NCI-H322M       | 30,895     | 4,429        | 4,425       | 4,394       | 4,420       | 4,402       | 4,410       | 4,415       | 4,058          | 4,130       | 5,458       | 4,251       | 4,648       | 4,249       | 4,101       | 4,391        | 4,420       | 4,389       | 4,416       | 4,468       | 4,406       | 4,405       | 6,881       | 7,188       | 3,378       | 2,053       | 5,591       | 1,718       | 4,086       |
| NCI-H460        | 31,050     | 4,446        | 4,442       | 4,419       | 4,435       | 4,461       | 4,455       | 4,392       | 4,101          | 4,147       | 5,482       | 4,249       | 4,658       | 4,279       | 4,134       | 4,398        | 4,489       | 4,458       | 4,447       | 4,439       | 4,389       | 4,430       | 6,839       | 7,141       | 3,445       | 2,088       | 5,682       | 1,718       | 4,137       |
| NCI-H522        | 29,232     | 4,185        | 4,179       | 4,193       | 4,214       | 4,143       | 4,152       | 4,166       | 3,910          | 3,901       | 5,203       | 4,020       | 4,401       | 3,963       | 3,834       | 4,243        | 4,232       | 4,209       | 4,193       | 4,153       | 4,071       | 4,131       | 6,456       | 6,802       | 3,250       | 1,917       | 5,241       | 1,651       | 3,915       |
| OVCAR-3         | 31,105     | 4,465        | 4,444       | 4,434       | 4,460       | 4,433       | 4,435       | 4,434       | 4,147          | 4,130       | 5,504       | 4,319       | 4,663       | 4,261       | 4,081       | 4,441        | 4,460       | 4,474       | 4,477       | 4,419       | 4,419       | 4,415       | 6,896       | 7,153       | 3,515       | 2,104       | 5,597       | 1,700       | 4,140       |
| OVCAR-4         | 30,423     | 4,359        | 4,374       | 4,335       | 4,326       | 4,352       | 4,341       | 4,336       | 4,016          | 4,057       | 5,342       | 4,221       | 4,574       | 4,185       | 4,028       | 4,292        | 4,391       | 4,400       | 4,392       | 4,327       | 4,306       | 4,315       | 6,703       | 7,079       | 3,387       | 2,037       | 5,484       | 1,687       | 4,046       |
| OVCAR-5         | 31,249     | 4,490        | 4,453       | 4,466       | 4,475       | 4,457       | 4,471       | 4,437       | 4,106          | 4,153       | 5,495       | 4,353       | 4,711       | 4,309       | 4,122       | 4,452        | 4,486       | 4,501       | 4,457       | 4,473       | 4,437       | 4,443       | 6,820       | 7,299       | 3,491       | 2,079       | 5,676       | 1,733       | 4,151       |
| OVCAR-8         | 32,050     | 4,607        | 4,566       | 4,575       | 4,574       | 4,577       | 4,576       | 4,575       | 4,222          | 4,277       | 5,665       | 4,415       | 4,811       | 4,405       | 4,255       | 4,570        | 4,612       | 4,579       | 4,568       | 4,598       | 4,553       | 4,570       | 7,086       | 7,402       | 3,628       | 2,101       | 5,815       | 1,751       | 4,267       |
| PC-3            | 24,187     | 3,441        | 3,440       | 3,487       | 3,439       | 3,461       | 3,477       | 3,442       | 3,130          | 3,221       | 4,165       | 3,376       | 3,682       | 3,404       | 3,209       | 3,446        | 3,476       | 3,529       | 3,461       | 3,391       | 3,455       | 3,429       | 5,328       | 6,238       | 2,742       | 1,576       | 3,908       | 1,467       | 2,928       |
| RPMI-8226       | 29,912     | 4,283        | 4,289       | 4,242       | 4,277       | 4,297       | 4,239       | 4,285       | 3,958          | 3,959       | 5,296       | 4,145       | 4,482       | 4,123       | 3,949       | 4,303        | 4,317       | 4,315       | 4,231       | 4,311       | 4,228       | 4,207       | 6,666       | 6,910       | 3,294       | 1,997       | 5,441       | 1,650       | 3,954       |
| RXF_393         | 28,620     | 4,067        | 4,083       | 4,129       | 4,090       | 4,108       | 4,069       | 4,074       | 3,695          | 3,817       | 5,061       | 3,956       | 4,340       | 3,913       | 3,838       | 4,136        | 4,096       | 4,094       | 4,054       | 4,077       | 4,090       | 4,073       | 6,216       | 6,673       | 3,201       | 1,874       | 5,227       | 1,615       | 3,814       |
| SF-268          | 31,647     | 4,549        | 4,547       | 4,505       | 4,516       | 4,516       | 4,516       | 4,498       | 4,179          | 4,221       | 5,583       | 4,388       | 4,770       | 4,329       | 4,177       | 4,508        | 4,577       | 4,563       | 4,482       | 4,522       | 4,495       | 4,500       | 7,033       | 7,370       | 3,436       | 2,089       | 5,811       | 1,722       | 4,186       |
| SF-295          | 31,678     | 4,534        | 4,505       | 4,537       | 4,535       | 4,537       | 4,522       | 4,508       | 4,196          | 4,236       | 5,577       | 4,390       | 4,753       | 4,336       | 4,190       | 4,495        | 4,537       | 4,578       | 4,527       | 4,488       | 4,515       | 4,538       | 7,049       | 7,303       | 3,565       | 2,125       | 5,697       | 1,738       | 4,201       |
| SF-539          | 30,125     | 4,348        | 4,276       | 4,272       | 4,314       | 4,308       | 4,319       | 4,288       | 3,997          | 3,990       | 5,350       | 4,174       | 4,493       | 4,114       | 4,007       | 4,270        | 4,403       | 4,399       | 4,314       | 4,258       | 4,226       | 4,255       | 6,662       | 6,950       | 3,277       | 1,999       | 5,571       | 1,662       | 4,004       |
| SK-MEL-2        | 29,932     | 4,304        | 4,273       | 4,254       | 4,274       | 4,299       | 4,278       | 4,250       | 3,923          | 3,985       | 5,326       | 4,156       | 4,473       | 4,108       | 3,961       | 4,268        | 4,301       | 4,327       | 4,241       | 4,278       | 4,245       | 4,272       | 6,645       | 6,925       | 3,289       | 1,971       | 5,523       | 1,664       | 3,915       |
| SK-MEL-28       | 31,373     | 4,531        | 4,486       | 4,467       | 4,485       | 4,464       | 4,493       | 4,447       | 4,151          | 4,195       | 5,530       | 4,353       | 4,719       | 4,278       | 4,147       | 4,459        | 4,569       | 4,483       | 4,459       | 4,481       | 4,461       | 4,461       | 6,928       | 7,230       | 3,542       | 2,102       | 5,716       | 1,696       | 4,159       |
| SK-MEL-5        | 31,199     | 4,477        | 4,458       | 4,453       | 4,446       | 4,452       | 4,466       | 4,447       | 4,143          | 4,151       | 5,499       | 4,322       | 4,678       | 4,295       | 4,111       | 4,489        | 4,484       | 4,504       | 4,402       | 4,417       | 4,443       | 4,460       | 6,866       | 7,234       | 3,543       | 2,098       | 5,618       | 1,729       | 4,111       |
| SK-OV-3         | 30,204     | 4,338        | 4,330       | 4,300       | 4,276       | 4,340       | 4,324       | 4,296       | 3,948          | 4,014       | 5,359       | 4,165       | 4,580       | 4,142       | 3,996       | 4,270        | 4,338       | 4,346       | 4,301       | 4,297       | 4,302       | 4,350       | 6,703       | 6,956       | 3,367       | 1,974       | 5,501       | 1,677       | 4,026       |
| SN12C           | 31,667     | 4,560        | 4,525       | 4,514       | 4,520       | 4,514       | 4,527       | 4,507       | 4,201          | 4,222       | 5,600       | 4,354       | 4,758       | 4,336       | 4,196       | 4,537        | 4,542       | 4,536       | 4,530       | 4,532       | 4,500       | 4,490       | 6,993       | 7,298       | 3,522       | 2,171       | 5,720       | 1,725       | 4,238       |
| SNB-19          | 31,436     | 4,525        | 4,501       | 4,482       | 4,489       | 4,496       | 4,478       | 4,465       | 4,143          | 4,190       | 5,529       | 4,334       | 4,741       | 4,330       | 4,169       | 4,464        | 4,530       | 4,490       | 4,476       | 4,475       | 4,489       | 4,512       | 6,937       | 7,257       | 3,533       | 2,079       | 5,689       | 1,745       | 4,196       |
| SNB-75          | 29,572     | 4,226        | 4,248       | 4,236       | 4,233       | 4,208       | 4,214       | 4,207       | 3,899          | 3,948       | 5,254       | 4,070       | 4,453       | 4,019       | 3,929       | 4,233        | 4,290       | 4,261       | 4,165       | 4,216       | 4,215       | 4,192       | 6,519       | 6,790       | 3,318       | 2,027       | 5,298       | 1,647       | 3,973       |
| SR              | 26,483     | 3,841        | 3,760       | 3,752       | 3,798       | 3,770       | 3,825       | 3,737       | 3,552          | 3,461       | 4,629       | 3,713       | 3,955       | 3,676       | 3,497       | 3,808        | 3,877       | 3,758       | 3,804       | 3,744       | 3,700       | 3,792       | 5,863       | 6,229       | 2,980       | 1,782       | 4,643       | 1,466       | 3,520       |
| SW-620          | 31,987     | 4,572        | 4,570       | 4,564       | 4,578       | 4,560       | 4,579       | 4,564       | 4,223          | 4,262       | 5,661       | 4,408       | 4,823       | 4,388       | 4,222       | 4,535        | 4,618       | 4,604       | 4,577       | 4,530       | 4,550       | 4,573       | 7,069       | 7,390       | 3,585       | 2,148       | 5,819       | 1,749       | 4,227       |
| T-47D           | 22,931     | 3,271        | 3,274       | 3,319       | 3,244       | 3,269       | 3,296       | 3,258       | 2,949          | 3,061       | 3,987       | 3,202       | 3,490       | 3,208       | 3,034       | 3,258        | 3,385       | 3,340       | 3,266       | 3,217       | 3,249       | 3,216       | 4,997       | 5,838       | 2,555       | 1,475       | 3,802       | 1,409       | 2,855       |
| TK-10           | 30,974     | 4,465        | 4,411       | 4,419       | 4,432       | 4,432       | 4,425       | 4,390       | 4,080          | 4,155       | 5,463       | 4,320       | 4,652       | 4,235       | 4,069       | 4,396        | 4,475       | 4,458       | 4,415       | 4,406       | 4,415       | 4,409       | 6,920       | 7,183       | 3,507       | 2,035       | 5,556       | 1,636       | 4,137       |
| U251            | 31,847     | 4,563        | 4,543       | 4,546       | 4,547       | 4,558       | 4,553       | 4,537       | 4,185          | 4,223       | 5,654       | 4,426       | 4,805       | 4,349       | 4,205       | 4,533        | 4,561       | 4,569       | 4,561       | 4,544       | 4,527       | 4,552       | 6,982       | 7,347       | 3,591       | 2,123       | 5,784       | 1,754       | 4,266       |
| UACC-257        | 31,544     | 4,481        | 4,507       | 4,521       | 4,495       | 4,529       | 4,528       | 4,483       | 4,136          | 4,216       | 5,574       | 4,366       | 4,733       | 4,318       | 4,201       | 4,464        | 4,530       | 4,534       | 4,515       | 4,526       | 4,488       | 4,487       | 6,939       | 7,292       | 3,549       | 2,093       | 5,750       | 1,719       | 4,202       |
| UACC-62         | 31,127     | 4,429        | 4,476       | 4,422       | 4,447       | 4,461       | 4,432       | 4,460       | 4,091          | 4,115       | 5,527       | 4,308       | 4,675       | 4,286       | 4,125       | 4,499        | 4,462       | 4,459       | 4,432       | 4,423       | 4,408       | 4,444       | 6,867       | 7,135       | 3,477       | 2,087       | 5,665       | 1,733       | 4,163       |
| UO-31           | 31,508     | 4,540        | 4,492       | 4,497       | 4,518       | 4,479       | 4,489       | 4,493       | 4,156          | 4,225       | 5,602       | 4,341       | 4,716       | 4,324       | 4,144       | 4,557        | 4,484       | 4,509       | 4,478       | 4,494       | 4,494       | 4,492       | 6,886       | 7,264       | 3,578       | 2,071       | 5,777       | 1,719       | 4,213       |

## Authors

- [@Rong830](https://www.github.com/Rong830)

## Contributing

Contributions are always welcome! If you'd like to contribute to this project, please follow the standard procedures:

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Make changes and commit
4. Push to your fork and submit a pull request

Please adhere to this project's `code of conduct`.

## Acknowledgments

Parts of this project are developed based on the GEM [^3] model from the [PaddleHelix repository](https://github.com/PaddlePaddle/PaddleHelix/tree/dev/apps/pretrained_compound/ChemRL/GEM) and the Transformer-CNN [^4] model from the [transformer-cnn repository](https://github.com/bigchem/transformer-cnn). We appreciate the PaddleHelix [@PaddlePaddle](https://www.github.com/PaddlePaddle) and [@bigchem](https://www.github.com/bigchem) teams' work and their contributions to the community.

[^3]: Fang, X., Liu, L., Lei, J. et al. Geometry-enhanced molecular representation learning for property prediction. Nat Mach Intell 4, 127–134 (2022). [https://doi.org/10.1038/s42256-021-00438-4](https://doi.org/10.1038/s42256-021-00438-4).

[^4]: Karpov, Pavel, et al. “Transformer-CNN: Swiss Knife for QSAR Modeling and Interpretation.” Journal of Cheminformatics, vol. 12, no. 1, Mar. 2020. Crossref, [ttps://doi.org/10.1186/s13321-020-00423-w](ttps://doi.org/10.1186/s13321-020-00423-w).

## Citation
If you use the code or data in this package, please cite:

```bibtex
@article{guo2024scaffold,
  title={Scaffold Splits Overestimate Virtual Screening Performance},
  author={Guo, Qianrong and Hernandez-Hernandez, Saiveth and Ballester, Pedro J},
  journal={arXiv preprint arXiv:2406.00873},
  year={2024}
}

@article{guo2024umap,
  title={UMAP-clustering split for rigorous evaluation of AI models for virtual screening on cancer cell lines},
  author={Guo, Qianrong and Hernandez-Hernandez, Saiveth and Ballester, Pedro J},
  journal={Journal of Cheminformatics},
  year={2024}
}

@conference{guo2024scaffoldsplits,
    author={Guo, Qianrong and Hernandez-Hernandez, Saiveth and Ballester, Pedro J.},
    editor={Wand, Michael and Malinovsk{\'a}, Krist{\'i}na and Schmidhuber, J{\"u}rgen and Tetko, Igor V.},
    title={Scaffold Splits Overestimate Virtual Screening Performance},
    booktitle={Artificial Neural Networks and Machine Learning -- ICANN 2024},
    year={2024},
    publisher={Springer Nature Switzerland},
    address={Cham},
    pages={58--72},
    isbn={978-3-031-72359-9}
}
```
