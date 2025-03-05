import numpy as np
from scipy import integrate

from lmfit import Parameters
from lmfit.models import LinearModel, GaussianModel, LorentzianModel, VoigtModel

from Orange.data import Table
from Orange.widgets import widget, gui
from Orange.widgets.utils.annotated_data import ANNOTATED_DATA_SIGNAL_NAME
from Orange.widgets.utils.signals import Input, Output

###
from orangecontrib.spectroscopy.data import getx, build_spec_table
import numpy as np

from orangecontrib.spectroscopy.data import getx, build_spec_table

# Copy from Acquisition Average .py file:
# import numpy as np

# import Orange.data

# Average Time-Resolved data by acquisition number
# data = in_data.copy()

# num_acqs, _ = data.get_column_view("Acquisition")
# num_acqs = int(num_acqs.max()) + 1
# print(f"Averaging {num_acqs} acquisitions.")
# hypercube = data.X.reshape((num_acqs, int(data.X.shape[0]/num_acqs), data.X.shape[1]))
# avg_hypercube = np.mean(hypercube, axis=0)

# n_domain = Orange.data.Domain(data.domain.attributes, data.domain.class_vars,
                              #[v for v in data.domain.metas if v.name != "Acquisition"])

# table = Orange.data.Table(n_domain, avg_hypercube, Y=None, metas=data.metas[0:avg_hypercube.shape[0],:-1])
# out_data = table


class OWAcquisitionAverage(widget.OWWidget):
    name = "IRsweep Acquisition Average"
    description = "Average IRsweep data by Acquisition Number"
    icon = "icons/category.svg"
    priority = 1020

    class Inputs:
        data = Input("Data", Table, default=True)

    class Outputs:
        fit = Output("Fit Parameters", Table, default=True)
        annotated_data = Output(ANNOTATED_DATA_SIGNAL_NAME, Table)

    def __init__(self):
        super().__init__()

        # GUI
        box = gui.widgetBox(self.controlArea, "Options")

    # if in_data and in_object:
    # data = in_data.copy()
    # calibration_data = in_object.copy()

    # new_wn_axis = add_lag_measurement(data, calibration_data)
    # assert len(new_wn_axis) == len(in_data.domain.attributes)

    # corrected_table = build_spec_table(new_wn_axis, in_data.X, in_data)
    # out_data = corrected_table
    # else:
    # print("Connect data to input / calibration data to object.")
    # out_data = None
    ###

    @Inputs.data
    def set_data(self, data):
        if data is not None:
            new_wn_axis = self.add_lag_measurement(data, object)
            # self.Outputs.fit.send(fit_data)
            self.Outputs.annotated_data.send(None)
        else:
            self.Outputs.fit.send(None)
            self.Outputs.annotated_data.send(None)


if __name__ == "__main__":  # pragma: no cover
    from Orange.widgets.utils.widgetpreview import WidgetPreview
    WidgetPreview(OWAcquisitionAverage).run(Table("collagen"))