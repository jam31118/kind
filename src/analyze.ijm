
/* MANIFEST
 - In default FIRSTIDX is set to 0, synced with camera python script
   This should be changed in future releases 
   to be able to be overwrited by arguments.
   Other parameters like PREFIX, FORMAT, IMGNUM etc. 
   will also be changed as mentioned above.
 - ...
*/

/*
HOME = getDirectory("home");
WORKDIR = HOME + "Pictures" + File.separator;
*/

argus = getArgument();
list = split(argus, '#');
WORKDIR = list[0] + File.separator;
PREFIX = "img";
FORMAT = "jpg";
IMGNUM = list[1];
FIRSTIDX = 1;
WAIT_TIME = 5000; // in millisecond;

print("Number of images: ",IMGNUM);
print("Starting Analysis . . .");

idx = FIRSTIDX;
while( idx < IMGNUM ) {
	if (idx > FIRSTIDX) { close(fileName(idx-1)); }
	fname = fileName(idx);
	if (fileExist(fname)) {
		open(fname);	
		print("Opened file: ",fname);
		analyze();
		save(saveName(idx));
		open(fname);
		idx++;
	}
	else {
		print("There is no file.."+fname+" waiting ",WAIT_TIME/1000);
		print("You can adjust waiting time if you want.");
		wait(WAIT_TIME);
	}
}

function fileExist(fname) {
	if( exec("ls",fname) != "" ) {return true;}
	else {return false;}
}
function saveName(idx) {
	save_fname = WORKDIR + "SAVED_" + PREFIX + idx + "." + FORMAT;
	return save_fname;
}
function fileName(idx) {
	fname = WORKDIR + PREFIX+idx+"."+FORMAT;
	return fname;
}
function analyze() {
	//run("Find Edges");
	run("8-bit");
	setThreshold(0, 90);
	setOption("BlackBackground", false);
	run("Set Measurements...", "center add redirect=None decimal=3");
	run("Analyze Particles...", "show=[Overlay Outlines] display clear");
	saveAs("Results", WORKDIR+"Results.xls");
}


