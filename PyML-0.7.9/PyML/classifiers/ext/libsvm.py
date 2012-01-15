# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.0
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_libsvm', [dirname(__file__)])
        except ImportError:
            import _libsvm
            return _libsvm
        if fp is not None:
            try:
                _mod = imp.load_module('_libsvm', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _libsvm = swig_import_helper()
    del swig_import_helper
else:
    import _libsvm
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


C_SVC = _libsvm.C_SVC
NU_SVC = _libsvm.NU_SVC
ONE_CLASS = _libsvm.ONE_CLASS
EPSILON_SVR = _libsvm.EPSILON_SVR
NU_SVR = _libsvm.NU_SVR
LINEAR = _libsvm.LINEAR
POLY = _libsvm.POLY
RBF = _libsvm.RBF
SIGMOID = _libsvm.SIGMOID
PRECOMPUTED = _libsvm.PRECOMPUTED
class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _libsvm.delete_SwigPyIterator
    __del__ = lambda self : None;
    def value(self): return _libsvm.SwigPyIterator_value(self)
    def incr(self, n = 1): return _libsvm.SwigPyIterator_incr(self, n)
    def decr(self, n = 1): return _libsvm.SwigPyIterator_decr(self, n)
    def distance(self, *args): return _libsvm.SwigPyIterator_distance(self, *args)
    def equal(self, *args): return _libsvm.SwigPyIterator_equal(self, *args)
    def copy(self): return _libsvm.SwigPyIterator_copy(self)
    def next(self): return _libsvm.SwigPyIterator_next(self)
    def __next__(self): return _libsvm.SwigPyIterator___next__(self)
    def previous(self): return _libsvm.SwigPyIterator_previous(self)
    def advance(self, *args): return _libsvm.SwigPyIterator_advance(self, *args)
    def __eq__(self, *args): return _libsvm.SwigPyIterator___eq__(self, *args)
    def __ne__(self, *args): return _libsvm.SwigPyIterator___ne__(self, *args)
    def __iadd__(self, *args): return _libsvm.SwigPyIterator___iadd__(self, *args)
    def __isub__(self, *args): return _libsvm.SwigPyIterator___isub__(self, *args)
    def __add__(self, *args): return _libsvm.SwigPyIterator___add__(self, *args)
    def __sub__(self, *args): return _libsvm.SwigPyIterator___sub__(self, *args)
    def __iter__(self): return self
SwigPyIterator_swigregister = _libsvm.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class DecisionFunction(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DecisionFunction, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DecisionFunction, name)
    __repr__ = _swig_repr
    __swig_setmethods__["numSV"] = _libsvm.DecisionFunction_numSV_set
    __swig_getmethods__["numSV"] = _libsvm.DecisionFunction_numSV_get
    if _newclass:numSV = _swig_property(_libsvm.DecisionFunction_numSV_get, _libsvm.DecisionFunction_numSV_set)
    __swig_setmethods__["numBSV"] = _libsvm.DecisionFunction_numBSV_set
    __swig_getmethods__["numBSV"] = _libsvm.DecisionFunction_numBSV_get
    if _newclass:numBSV = _swig_property(_libsvm.DecisionFunction_numBSV_get, _libsvm.DecisionFunction_numBSV_set)
    __swig_setmethods__["svID"] = _libsvm.DecisionFunction_svID_set
    __swig_getmethods__["svID"] = _libsvm.DecisionFunction_svID_get
    if _newclass:svID = _swig_property(_libsvm.DecisionFunction_svID_get, _libsvm.DecisionFunction_svID_set)
    __swig_setmethods__["alpha"] = _libsvm.DecisionFunction_alpha_set
    __swig_getmethods__["alpha"] = _libsvm.DecisionFunction_alpha_get
    if _newclass:alpha = _swig_property(_libsvm.DecisionFunction_alpha_get, _libsvm.DecisionFunction_alpha_set)
    __swig_setmethods__["rho"] = _libsvm.DecisionFunction_rho_set
    __swig_getmethods__["rho"] = _libsvm.DecisionFunction_rho_get
    if _newclass:rho = _swig_property(_libsvm.DecisionFunction_rho_get, _libsvm.DecisionFunction_rho_set)
    def __init__(self): 
        this = _libsvm.new_DecisionFunction()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _libsvm.delete_DecisionFunction
    __del__ = lambda self : None;
DecisionFunction_swigregister = _libsvm.DecisionFunction_swigregister
DecisionFunction_swigregister(DecisionFunction)

class svm_node(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, svm_node, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, svm_node, name)
    __repr__ = _swig_repr
    __swig_setmethods__["index"] = _libsvm.svm_node_index_set
    __swig_getmethods__["index"] = _libsvm.svm_node_index_get
    if _newclass:index = _swig_property(_libsvm.svm_node_index_get, _libsvm.svm_node_index_set)
    __swig_setmethods__["value"] = _libsvm.svm_node_value_set
    __swig_getmethods__["value"] = _libsvm.svm_node_value_get
    if _newclass:value = _swig_property(_libsvm.svm_node_value_get, _libsvm.svm_node_value_set)
    def __init__(self): 
        this = _libsvm.new_svm_node()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _libsvm.delete_svm_node
    __del__ = lambda self : None;
svm_node_swigregister = _libsvm.svm_node_swigregister
svm_node_swigregister(svm_node)

class svm_problem(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, svm_problem, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, svm_problem, name)
    __repr__ = _swig_repr
    __swig_setmethods__["l"] = _libsvm.svm_problem_l_set
    __swig_getmethods__["l"] = _libsvm.svm_problem_l_get
    if _newclass:l = _swig_property(_libsvm.svm_problem_l_get, _libsvm.svm_problem_l_set)
    __swig_setmethods__["y"] = _libsvm.svm_problem_y_set
    __swig_getmethods__["y"] = _libsvm.svm_problem_y_get
    if _newclass:y = _swig_property(_libsvm.svm_problem_y_get, _libsvm.svm_problem_y_set)
    __swig_setmethods__["x"] = _libsvm.svm_problem_x_set
    __swig_getmethods__["x"] = _libsvm.svm_problem_x_get
    if _newclass:x = _swig_property(_libsvm.svm_problem_x_get, _libsvm.svm_problem_x_set)
    def __init__(self): 
        this = _libsvm.new_svm_problem()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _libsvm.delete_svm_problem
    __del__ = lambda self : None;
svm_problem_swigregister = _libsvm.svm_problem_swigregister
svm_problem_swigregister(svm_problem)

class svm_parameter(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, svm_parameter, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, svm_parameter, name)
    __repr__ = _swig_repr
    __swig_setmethods__["svm_type"] = _libsvm.svm_parameter_svm_type_set
    __swig_getmethods__["svm_type"] = _libsvm.svm_parameter_svm_type_get
    if _newclass:svm_type = _swig_property(_libsvm.svm_parameter_svm_type_get, _libsvm.svm_parameter_svm_type_set)
    __swig_setmethods__["kernel_type"] = _libsvm.svm_parameter_kernel_type_set
    __swig_getmethods__["kernel_type"] = _libsvm.svm_parameter_kernel_type_get
    if _newclass:kernel_type = _swig_property(_libsvm.svm_parameter_kernel_type_get, _libsvm.svm_parameter_kernel_type_set)
    __swig_setmethods__["degree"] = _libsvm.svm_parameter_degree_set
    __swig_getmethods__["degree"] = _libsvm.svm_parameter_degree_get
    if _newclass:degree = _swig_property(_libsvm.svm_parameter_degree_get, _libsvm.svm_parameter_degree_set)
    __swig_setmethods__["gamma"] = _libsvm.svm_parameter_gamma_set
    __swig_getmethods__["gamma"] = _libsvm.svm_parameter_gamma_get
    if _newclass:gamma = _swig_property(_libsvm.svm_parameter_gamma_get, _libsvm.svm_parameter_gamma_set)
    __swig_setmethods__["coef0"] = _libsvm.svm_parameter_coef0_set
    __swig_getmethods__["coef0"] = _libsvm.svm_parameter_coef0_get
    if _newclass:coef0 = _swig_property(_libsvm.svm_parameter_coef0_get, _libsvm.svm_parameter_coef0_set)
    __swig_setmethods__["cache_size"] = _libsvm.svm_parameter_cache_size_set
    __swig_getmethods__["cache_size"] = _libsvm.svm_parameter_cache_size_get
    if _newclass:cache_size = _swig_property(_libsvm.svm_parameter_cache_size_get, _libsvm.svm_parameter_cache_size_set)
    __swig_setmethods__["eps"] = _libsvm.svm_parameter_eps_set
    __swig_getmethods__["eps"] = _libsvm.svm_parameter_eps_get
    if _newclass:eps = _swig_property(_libsvm.svm_parameter_eps_get, _libsvm.svm_parameter_eps_set)
    __swig_setmethods__["C"] = _libsvm.svm_parameter_C_set
    __swig_getmethods__["C"] = _libsvm.svm_parameter_C_get
    if _newclass:C = _swig_property(_libsvm.svm_parameter_C_get, _libsvm.svm_parameter_C_set)
    __swig_setmethods__["nr_weight"] = _libsvm.svm_parameter_nr_weight_set
    __swig_getmethods__["nr_weight"] = _libsvm.svm_parameter_nr_weight_get
    if _newclass:nr_weight = _swig_property(_libsvm.svm_parameter_nr_weight_get, _libsvm.svm_parameter_nr_weight_set)
    __swig_setmethods__["weight_label"] = _libsvm.svm_parameter_weight_label_set
    __swig_getmethods__["weight_label"] = _libsvm.svm_parameter_weight_label_get
    if _newclass:weight_label = _swig_property(_libsvm.svm_parameter_weight_label_get, _libsvm.svm_parameter_weight_label_set)
    __swig_setmethods__["weight"] = _libsvm.svm_parameter_weight_set
    __swig_getmethods__["weight"] = _libsvm.svm_parameter_weight_get
    if _newclass:weight = _swig_property(_libsvm.svm_parameter_weight_get, _libsvm.svm_parameter_weight_set)
    __swig_setmethods__["nu"] = _libsvm.svm_parameter_nu_set
    __swig_getmethods__["nu"] = _libsvm.svm_parameter_nu_get
    if _newclass:nu = _swig_property(_libsvm.svm_parameter_nu_get, _libsvm.svm_parameter_nu_set)
    __swig_setmethods__["p"] = _libsvm.svm_parameter_p_set
    __swig_getmethods__["p"] = _libsvm.svm_parameter_p_get
    if _newclass:p = _swig_property(_libsvm.svm_parameter_p_get, _libsvm.svm_parameter_p_set)
    __swig_setmethods__["shrinking"] = _libsvm.svm_parameter_shrinking_set
    __swig_getmethods__["shrinking"] = _libsvm.svm_parameter_shrinking_get
    if _newclass:shrinking = _swig_property(_libsvm.svm_parameter_shrinking_get, _libsvm.svm_parameter_shrinking_set)
    __swig_setmethods__["probability"] = _libsvm.svm_parameter_probability_set
    __swig_getmethods__["probability"] = _libsvm.svm_parameter_probability_get
    if _newclass:probability = _swig_property(_libsvm.svm_parameter_probability_get, _libsvm.svm_parameter_probability_set)
    def __init__(self): 
        this = _libsvm.new_svm_parameter()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _libsvm.delete_svm_parameter
    __del__ = lambda self : None;
svm_parameter_swigregister = _libsvm.svm_parameter_swigregister
svm_parameter_swigregister(svm_parameter)


def svm_train_one_pyml(*args):
  return _libsvm.svm_train_one_pyml(*args)
svm_train_one_pyml = _libsvm.svm_train_one_pyml
class intArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, intArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, intArray, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _libsvm.new_intArray(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _libsvm.delete_intArray
    __del__ = lambda self : None;
    def __getitem__(self, *args): return _libsvm.intArray___getitem__(self, *args)
    def __setitem__(self, *args): return _libsvm.intArray___setitem__(self, *args)
    def cast(self): return _libsvm.intArray_cast(self)
    __swig_getmethods__["frompointer"] = lambda x: _libsvm.intArray_frompointer
    if _newclass:frompointer = staticmethod(_libsvm.intArray_frompointer)
intArray_swigregister = _libsvm.intArray_swigregister
intArray_swigregister(intArray)

def intArray_frompointer(*args):
  return _libsvm.intArray_frompointer(*args)
intArray_frompointer = _libsvm.intArray_frompointer

class doubleArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, doubleArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, doubleArray, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _libsvm.new_doubleArray(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _libsvm.delete_doubleArray
    __del__ = lambda self : None;
    def __getitem__(self, *args): return _libsvm.doubleArray___getitem__(self, *args)
    def __setitem__(self, *args): return _libsvm.doubleArray___setitem__(self, *args)
    def cast(self): return _libsvm.doubleArray_cast(self)
    __swig_getmethods__["frompointer"] = lambda x: _libsvm.doubleArray_frompointer
    if _newclass:frompointer = staticmethod(_libsvm.doubleArray_frompointer)
doubleArray_swigregister = _libsvm.doubleArray_swigregister
doubleArray_swigregister(doubleArray)

def doubleArray_frompointer(*args):
  return _libsvm.doubleArray_frompointer(*args)
doubleArray_frompointer = _libsvm.doubleArray_frompointer


