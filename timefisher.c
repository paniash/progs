#include <apop.h>
int main()
{
    inti, test_ct = 5e6;
    double data[] = {30, 86, 24, 38};
    apop_data *testdata = apop_line_to_data(data, 0, 2, 2);
    for (i = 0; i<test_ct; i++)
        apop_test_fisher_exact(testdata);
}
