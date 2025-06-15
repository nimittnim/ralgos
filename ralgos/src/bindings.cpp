#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "generators/kuniform.h"
#include "generators/uuniform.h"
#include "generators/uniform.h"
#include "generators/normal.h"
#include "generators/bernoulli.h"
#include "generators/kbernoulli.h"
#include "generators/margulis.h"

namespace py = pybind11;

PYBIND11_MODULE(ralgos_cpp, m) {
    py::class_<KUniformGenerator>(m, "KUniformGenerator")
        .def(py::init<int, int, int>(), py::arg("k"), py::arg("p"),py::arg("m"))
        .def("sample", &KUniformGenerator::sample);

    py::class_<UUniformGenerator>(m, "UUniformGenerator")
        .def(py::init<int,int>(),py::arg("p"),py::arg("m"))
        .def("sample",&UUniformGenerator::sample);

    py::class_<UniformGenerator>(m, "UniformGenerator")
    .def(py::init<int>(), py::arg("m"))
    .def("sample", &UniformGenerator::sample);

    py::class_<NormalGenerator>(m, "NormalGenerator")
        .def(py::init<double, double>(), 
            py::arg("mean"), py::arg("std"))
        .def("sample", &NormalGenerator::sample);

    py::class_<BernoulliGenerator>(m, "BernoulliGenerator")
    .def(py::init<double>(), py::arg("p"))
    .def("sample", &BernoulliGenerator::sample);

    py::class_<KBernoulliGenerator>(m, "KBernoulliGenerator")
        .def(py::init<int, double, int>(), py::arg("k"), py::arg("p_"),py::arg("p"))
        .def("sample", &KBernoulliGenerator::sample);

    py::class_<MargulisGenerator>(m, "MargulisGenerator")
        .def(py::init<int, int>(), py::arg("v"), py::arg("m"))
        .def("sample", &MargulisGenerator::sample);
}
