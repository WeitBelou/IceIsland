// Domain identifiers
BOTTOM_SEDIMENTS = 1;
FIRST_DENSE_LAYER = 2;
SECOND_DENSE_LAYER = 3;
CRYSTAL_FOUNDATION = 4;

BOTTOM_SURFACE = 1;

// Units
METER = 1;
KILOMETER = 1000 * METER;

size = 10 * KILOMETER;
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

