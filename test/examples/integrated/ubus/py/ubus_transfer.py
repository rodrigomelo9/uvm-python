#//----------------------------------------------------------------------
#//   Copyright 2007-2010 Mentor Graphics Corporation
#//   Copyright 2007-2010 Cadence Design Systems, Inc.
#//   Copyright 2010 Synopsys, Inc.
#//   Copyright 2019 Tuomas Poikela (tpoikela)
#//   All Rights Reserved Worldwide
#//
#//   Licensed under the Apache License, Version 2.0 (the
#//   "License"); you may not use this file except in
#//   compliance with the License.  You may obtain a copy of
#//   the License at
#//
#//       http://www.apache.org/licenses/LICENSE-2.0
#//
#//   Unless required by applicable law or agreed to in
#//   writing, software distributed under the License is
#//   distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
#//   CONDITIONS OF ANY KIND, either express or implied.  See
#//   the License for the specific language governing
#//   permissions and limitations under the License.
#//----------------------------------------------------------------------

from uvm.seq import UVMSequenceItem
from uvm.macros import *

#//------------------------------------------------------------------------------
#//
#// ubus transfer enums, parameters, and events
#//
#//------------------------------------------------------------------------------

#typedef enum { NOP,
#               READ,
#               WRITE
#             } ubus_read_write_enum;
NOP = 0
READ = 1
WRITE = 2


#//------------------------------------------------------------------------------
#//
#// CLASS: ubus_transfer
#//
#//------------------------------------------------------------------------------

class ubus_transfer(UVMSequenceItem):

    # TODO add these constraints
    #  constraint c_read_write {
    #    read_write inside { READ, WRITE };
    #  }
    #  constraint c_size {
    #    size inside {1,2,4,8};
    #  }
    #  constraint c_data_wait_size {
    #    data.size() == size;
    #    wait_state.size() == size;
    #  }
    #  constraint c_transmit_delay {
    #    transmit_delay <= 10 ;
    #  }

    def __init__(self, name="ubus_transfer_inst"):
        UVMSequenceItem.__init__(self, name)
        self.addr = 0
        self.rand("addr")
        self.read_write = 0
        self.rand("read_write")
        self.size = 0
        self.rand("size")
        self.data = []
        self.rand("data")
        self.wait_state = []
        self.rand("wait_state")
        self.error_pos = 0
        self.rand("error_pos")
        self.transmit_delay = 0
        self.rand("transmit_delay")
        self.master = ""
        self.slave = ""


    def convert2string(self):
        res = "addr: " + str(self.addr) + ", read_write: " + str(self.read_write)
        res += ", size: " + str(self.size) + ", wait_state: " + str(self.wait_state)
        res += "\ndata: " + str(self.data)
        return res
    #endclass : ubus_transfer

uvm_object_utils(ubus_transfer)

# TODO implement the field macros
#  `uvm_object_utils_begin(ubus_transfer)
#    `uvm_field_int      (addr,           UVM_DEFAULT)
#    `uvm_field_enum     (ubus_read_write_enum, read_write, UVM_DEFAULT)
#    `uvm_field_int      (size,           UVM_DEFAULT)
#    `uvm_field_array_int(data,           UVM_DEFAULT)
#    `uvm_field_array_int(wait_state,     UVM_DEFAULT)
#    `uvm_field_int      (error_pos,      UVM_DEFAULT)
#    `uvm_field_int      (transmit_delay, UVM_DEFAULT)
#    `uvm_field_string   (master,         UVM_DEFAULT|UVM_NOCOMPARE)
#    `uvm_field_string   (slave,          UVM_DEFAULT|UVM_NOCOMPARE)
#  `uvm_object_utils_end
