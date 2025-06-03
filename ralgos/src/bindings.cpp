#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "kwise.cpp"

namespace py = pybind11;

PYBIND11_MODULE(ralgos_cpp, m) {
    py::class_<KwiseGenerator>(m, "KwiseGenerator")
        .def(py::init<int, int>(), py::arg("k"), py::arg("seed"))
        .def("sample", &KwiseGenerator::sample);
}
