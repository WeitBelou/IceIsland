// Domain identifiers
BOTTOM_SEDIMENTS = 1;
FIRST_DENSE_LAYER = 2;
SECOND_DENSE_LAYER = 3;
CRYSTAL_FOUNDATION = 4;

BOTTOM_SURFACE = 1;

// Units
METER = 1;
KILOMETER = 1000 * METER;

size = 4 * KILOMETER;
a = size / 2;

// Bottom
Point(1) = {-a, -a, 0};
Point(2) = {a, -a, 0};
Point(3) = {a, a, 0};
Point(4) = {-a, a, 0};

Line(1) = {1, 2};
Line(2) = {2, 3};
Line(3) = {3, 4};
Line(4) = {4, 1};

Line Loop(1) = {1, 2, 3, 4};
Plane Surface(1) = {1};
Physical Surface(BOTTOM_SURFACE) = {1};

// Crystal foundation
h_crystal = 1 * KILOMETER;
out[] = Extrude {0, 0, h_crystal} {
  Surface{1};
};
crystal_top = out[0];
Physical Volume(CRYSTAL_FOUNDATION) = {out[1]};
Delete out;

// Second dense layer
h_dense_2 = 400 * METER;
out[] = Extrude {0, 0, h_dense_2} {
  Surface{crystal_top};
};
dense_2_top = out[0];
Physical Volume(SECOND_DENSE_LAYER) = {out[1]};
Delete out;

// First dense layer
h_dense_1 = 300 * METER;
out[] = Extrude {0, 0, h_dense_1} {
  Surface{dense_2_top};
};
dense_1_top = out[0];
Physical Volume(FIRST_DENSE_LAYER) = {out[1]};
Delete out;

// Sediments
h_sediments = 50 * METER;
out[] = Extrude {0, 0, h_sediments} {
  Surface{dense_1_top};
};
sediments_top = out[0];
Physical Volume(BOTTOM_SEDIMENTS) = {out[1]};
Delete out;

// Mesh options

Field[1] = MathEval;
Field[1].F = "25.0";

Field[2] = Restrict;
Field[2].IField = 1;
Field[2].FacesList = {sediments_top, dense_1_top};

Field[3] = MathEval;
Field[3].F = "50.0";

Field[4] = Restrict;
Field[4].IField = 3;
Field[4].FacesList = {dense_2_top};

Field[5] = MathEval;
Field[5].F = "50.0";

Field[6] = Restrict;
Field[6].IField = 5;
Field[6].FacesList = {crystal_top};

Field[7] = MathEval;
Field[7].F = "100.0";

Field[8] = Restrict;
Field[8].IField = 7;
Field[8].RegionsList = {BOTTOM_SURFACE};

Field[10] = Min;
Field[10].FieldsList = {2, 4, 6, 8};

Background Field = 10;
