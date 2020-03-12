REM https://blog.csdn.net/sylsjane/article/details/83751297

REM create mogu.font_properties with line: mogu 0 0 0 0 0
REM generate mogu.box with the following command before running this bat, then correction in jTessBoxEditor (Box Editor, modify Character/X/Y/W/H, then save for each char!)
REM tesseract mogu.tif mogu --psm 10 batch.nochop makebox

if "%2" == "" (
  echo "Usage: train.bat dir lang"
  exit /b
)

cd %1

set lang=%2

REM generate mogu.tr
tesseract %lang%.tif %lang% --psm 10 nobatch box.train

REM generate unicharset
unicharset_extractor %lang%.box

REM generate shapetable
shapeclustering -F %lang%.font_properties -U unicharset %lang%.tr

REM generate inttemp/pffmtable/unicharset/shapetable(if not exists), add "mogu." prefix
mftraining -F %lang%.font_properties -U unicharset -O %lang%.unicharset %lang%.tr

REM generate normproto, add "mogu." prefix
cntraining %lang%.tr

ren normproto %lang%.normproto 
ren inttemp %lang%.inttemp 
ren pffmtable %lang%.pffmtable 
ren shapetable %lang%.shapetable 

REM generate traineddata
combine_tessdata %lang%

REM if not move traineddata, need to specify –tessdata-dir when calling tesseract