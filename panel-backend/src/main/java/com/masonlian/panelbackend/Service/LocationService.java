package com.masonlian.panelbackend.Service;


import com.masonlian.panelbackend.Dto.FinalLocationJournal;
import com.masonlian.panelbackend.Dto.LocationJournal;
import com.masonlian.panelbackend.request.LocationData;
import org.springframework.stereotype.Component;

import java.util.List;

@Component
public interface LocationService {
    Integer  enrollLocation(LocationData locationData);
    FinalLocationJournal getJournalById(Integer journalId);
    List<FinalLocationJournal> getJournalByDate(String month, String day);


}
