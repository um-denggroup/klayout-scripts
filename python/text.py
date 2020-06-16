import pya

def create(ly, li, text, mag, flatten=False):
    """Add text.

    ly:         Layout object
    li:         layer index
    text:       text content
    mag:        magnification
    flatten:    False: return CellInstArray object (default)
                True: return Region object
    """
    
    # finding the PCell declaration object ...
    lib = pya.Library.library_by_name("Basic")
    if lib == None:
        raise Exception("Unknown lib 'Basic'")
    pcell_decl = lib.layout().pcell_declaration("TEXT");
    if pcell_decl == None:
        raise Exception("Unknown PCell 'TEXT'")
    
    # translating named parameters into an ordered sequence ...
    # named parameters
    param = { 
        "text": text, 
        "layer": ly.get_info(li),  # target layer of the text
        "mag": mag 
    }
    
    # translate to array (to pv)
    pv = []
    for p in pcell_decl.get_parameters():
        if p.name in param:
            pv.append(param[p.name])
        else:
            pv.append(p.default)
    
    # create the PCell variant cell
    pcell_var = ly.add_pcell_variant(lib, pcell_decl.id(), pv)
    
    if not flatten:
        # transformation
        t = pya.Trans()
        # insert into "top_cell" (must be provided by the caller)
        return pya.CellInstArray(pcell_var, t)
    else:
        # collect shapes
        reg = pya.Region(ly.cell(pcell_var).begin_shapes_rec(li))
        return reg
