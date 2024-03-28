#Author - Richard McQuiston
#Description - Calculate remaining values for a triangle given three inputs
#Version 1.0.0

import adsk.core, adsk.fusion, adsk.cam, traceback
import math as mt

def radToDeg(x):
    grados=x*180/mt.pi
    return grados
command_cache = {}
def get(obj, key, default=None):
    if type(obj) in command_cache and key in command_cache[type(obj)]:
        return command_cache[type(obj)][key]
    return default
def set(obj_type, key, value):
    global command_cache
    if obj_type not in command_cache:
        command_cache[obj_type] = {}
    command_cache[obj_type][key] = value
def save_params(command_type, command_inputs):
    for i in range(int(command_inputs.count)):
        try:
            input = command_inputs.item(i)
            if type(input) not in [adsk.core.ButtonRowCommandInput, adsk.core.DropDownCommandInput]:
                val = input.value
                if hasattr(input, 'unitType') and input.unitType == 'deg':
                    val = radToDeg(val)
                set(command_type, input.id, val)
        except Exception as e:
            print('Exception')
            print(e)
class cmdDefOKButtonPressedEventHandler(adsk.core.CommandEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self,args):
        try:
            eventArgs=adsk.core.CommandEventArgs.cast(args)
            app=adsk.core.Application.get()
            ui=app.userInterface
            design = app.activeProduct
            inputs2 = eventArgs.command.commandInputs

            sA = inputs2.itemById('SideA').value
            sB = inputs2.itemById('SideB').value
            sC = inputs2.itemById('SideC').value

            aA = inputs2.itemById('AngleA').value
            aB = inputs2.itemById('AngleB').value
            aC = inputs2.itemById('AngleC').value

            save_params(cmdDefPressedEventHandler, inputs2)


        except:
            if ui:
                ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
# Event handler for the inputChanged event.
class ExternalGear_ChangedHandler(adsk.core.InputChangedEventHandler):
    def __init__(self):
        super().__init__()

    def notify(self, args):
        app = adsk.core.Application.get()
        ui = app.userInterface
        try:
            eventArgs = adsk.core.InputChangedEventArgs.cast(args)

            # Gets the command input that was changed and its parent's command inputs
            changedInput = eventArgs.input
            inputs2 = changedInput.parentCommand.commandInputs

        except:
            if ui:
                ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
class cmdDefPressedEventHandler(adsk.core.CommandCreatedEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        app = adsk.core.Application.get()
        ui = app.userInterface
        cmd = args.command
        inputs = cmd.commandInputs
        cmd.isExecutedWhenPreEmpted = False

        inputs.addValueInput('SideA', 'Side A [mm]', 'mm', adsk.core.ValueInput.createByReal(get(self, 'SideA', 0.00)))
        inputs.addValueInput('SideB', 'Side B [mm]', 'mm', adsk.core.ValueInput.createByReal(get(self, 'SideB', 0.00)))
        inputs.addValueInput('SideC', 'Side C [mm]', 'mm', adsk.core.ValueInput.createByReal(get(self, 'SideC', 0.00)))

        inputs.addValueInput('AngleA', 'Angle A [°]', 'deg',
                             adsk.core.ValueInput.createByReal(get(self, 'AngleA', 0)))
        inputs.addValueInput('AngleB', 'Angle B [°]', 'deg',
                             adsk.core.ValueInput.createByReal(get(self, 'AngleB', 0)))
        inputs.addValueInput('AngleC', 'Angle C [°]', 'deg',
                             adsk.core.ValueInput.createByReal(get(self, 'AngleC', 0)))

        # When any input changes, the following handler triggers
        onInputChanged = ExternalGear_ChangedHandler()
        cmd.inputChanged.add(onInputChanged)
        handlers.append(onInputChanged)

        # con esto vinculo al boton OK
        onExecute = cmdDefOKButtonPressedEventHandler()
        cmd.execute.add(onExecute)
        handlers.append(onExecute)

tbPanel = None
def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface

        workSpace = ui.workspaces.itemById('FusionSolidEnvironment')
        tbPanels = workSpace.toolbarPanels

        global tbPanel
        tbPanel = tbPanels.itemById('NewPanel')
        if tbPanel:
            tbPanel.deleteMe()
        tbPanel = tbPanels.add('NewPanel', 'Triangle Calculator', 'SelectPanel', False)

        ui.messageBox('Hello script')

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
def stop(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        if tbPanel:
            tbPanel.deleteMe()
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))